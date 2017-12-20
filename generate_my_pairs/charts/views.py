from django.shortcuts import render

import charts.backends.Calculate as Calc
from reportlab.pdfgen import canvas
from generate_my_pairs.models import Post
from generate_my_pairs.views import handle_uploaded_file, populate_file


def show_diff_tech(request):
    my_file = Post.objects.last()#Post.objects.order_by('-id')[0]
    latest_uploaded_file = my_file.file
    print("suan show_diff_tech" + str(latest_uploaded_file))
    print("suan show_diff_tech TYPE" + str(type(latest_uploaded_file)))

    if request.method == 'POST':
        technique = request.POST['select_techniques']
        print("Selected technique is " + str(technique))
        parameters = populate_file(latest_uploaded_file)
        params = parameters
        c = Calc.Calculate(parameters)
        if technique == "linear_programming":
            proposal = c.get_proposal_with_linear_programming(parameters)
        elif technique == "simulated_annealing":
            proposal = c.get_proposal_with_simulated_annealing(parameters)
        print("proposalllllll  :  " + str(proposal.values()))
        proposal_result = proposal
        print(proposal_result)
        number_of_test_cases = sum(proposal_result.values())
        args = {'selected_technique' : technique,
                'proposals': proposal_result,
                'number_of_test_cases': number_of_test_cases}
        return render(request, "charts.html", args)
