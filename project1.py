import speech_recognition as sr
r1= sr.Recognizer()
r2= sr.Recognizer()
r3= sr.Recognizer()
with sr.Microphone() as source:
    print('search edureka: search youtube]')
    print('speak now')
    audio=r3.listen(source)
    if 'video' in r2.recognize_google(audio):
        r2 = sr.Recognizer()
        url="https//www.youtube.co/"
        with sr.Microphone() as source:
            print('search your query ')
            audio=r2.listen(source)
            try:
                get=r2.recognize_google(audio)
                print(get)
                wb.get().open_new(url+get)
            except sr.UnknownvalueError:
                    print('error')
            except sr.RequestError as e:
                print('failed' .forat(e))

if 'video' in rl.recognize_google(audio):
    rl = sr.Recognizer()
    url='https://www.youtube.co/results?search_query='
    with sr.Microphone() as source:
        print('search for a video')
        audio=r2.listen(source)
        try:
            get=r1.reconize_google(audio)
            print(get)
            wb.gwt().open_new1(url+get)

        except sr.UnknownValueError:
            print('cloud not understand')

        except sr.RequestError as e:
            print('failed to get results' . format(e))
                     

         
                    

