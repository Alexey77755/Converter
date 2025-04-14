from django.shortcuts import render, redirect
from .models import Audio
from convert_video_to_audio_text.Out_Audio import vidioConvert
from convert_video_to_audio_text.forms import AudioForm
#import pdb

# Create your views here.
def audio_function(request):
    """Добавляет новую запись по конкретной теме."""

    if request.method == 'GET':
        form = AudioForm()
        print("открыл страницу")
        # Данные не отправлялись; создается пустая форма.
    elif request.method == 'POST':
        # Отправлены данные POST; обработать данные.
        form = AudioForm(data=request.POST)
        if form.is_valid():
            # pdb.set_trace()
            # Audio.objects.all().delete()
            form.save()
            # pdb.set_trace()
            print("получил данные")
            audio = Audio.objects.all()
            # print(audio)
            #pdb.set_trace()

            # print (audio[0])
            if audio[0] is not None:
                vidioConvert(str(audio[0]))
                Audio.objects.all().delete()
                return redirect('video_In_audio:audioWiews')

    # Вывести пустую или недействительную форму.
    # context = {'topic': topic, 'form': form}
    context = {'form': form}
    return render(request, 'audio.html', context)
