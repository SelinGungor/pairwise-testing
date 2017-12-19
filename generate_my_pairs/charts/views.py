from django.shortcuts import render


from reportlab.pdfgen import canvas
from django.http import HttpResponse
#
#
# def show_diff_tech(request):
#     if request.method == 'POST':
#         list = request.POST.getlist('services')
#         print("select_techniques : " + list)
#         # if form.is_valid():
#         #     posts = Post.objects.all()
#         #     for x in posts:
#         #         print("Selin : " +str(x))
#         #     myyfile = request.FILES['file']
#         #     print("Deniz : " + str(myyfile.name))
#         #     print(str(myyfile))
#         #     print(type(myyfile))
#         #     handle_uploaded_file(myyfile, "data.csv")
#         #     form.save()
#         #     parameters = populate_file("data.csv")
#         #
#         #     # if file:
#         #     #     print ("**found file" + file.filename)
#         #     #     filename = secure_filename(file.filename)
#         #     #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         #     print(type(parameters))
#         #     print(parameters)
#         #     params = parameters
#         #     c = calc.Calculate(parameters)
#         #     proposal = c.get_proposal_with_linear_programming(parameters)
#         #     print("proposalllllll  :  "+ str(proposal.values()))
#         #     proposal_result = proposal
#         #     print(proposal_result)
#         #     number_of_test_cases = sum(proposal_result.values())
#         args = {'form': form,
#                 'proposals': proposal_result,
#                 'number_of_test_cases': number_of_test_cases}
#     return render(request, "charts.html", args)