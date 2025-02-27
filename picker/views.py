from django.shortcuts import render
global model


def mainpage(request):
    return render(request, 'picker/mainpage.html')


def inputPage(request):
    return render(request, 'picker/inputpage.html')


def resultPage(request):
    if request.method == "POST":
        score = float(request.POST['score'])
        if score >= 0.7:
            resultMsg = "이건 로코의 퍼스널리티에 저스트-핏! 이네요! 확실해요!"
        elif score >= 0.5:
            resultMsg = "흠.. 조금 낫-클리어하긴 하지만.. 로코의 퍼스널리티의 필링이네요!"
        elif score >= 0.3:
            resultMsg = "이건 로코의 인스피레이션이라기에는 낫-클리어 하네요..."
        else:
            resultMsg = ".. 이건 로코의 포트레이트는 아니네요!"

        result = [score, float(request.POST['score2'])]
        percentage = score * 100
        frame_b64 = request.POST['imageForm']



        return render(request, 'picker/resultPage.html', {'percentage':percentage, 'image':frame_b64, 'resultMsg':resultMsg, 'result':result})
        # ------------------ 서버에서 모델 처리 ---------------------------
        # if 'image' in request.FILES:
        #     try:
        #         model
        #     except NameError:
        #         model = predictapp.load_model()

        #     data = request.FILES['image']
        #     result, frame_b64, percentage, msg = predictapp.predict(model, data)
        # return render(request, 'picker/resultPage.html', {'image':frame_b64, 'result':result, 'percentage':percentage, 'resultMsg':msg})
        # -------------------------------------------------------

    return render(request, 'picker/error.html')


def creditPage(request):

    return render(request, 'picker/creditPage.html')


def errorPage(request):
    return render(request, 'picker/error.html')


def error404(request, exception):
    return render(request, 'picker/error.html', status=404)


def error500(request):
    return render(request, 'picker/error.html', status=500)
