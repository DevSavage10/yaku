# 끝말잇기 한방단어 검색 Python
끝말잇기 한방 단어 검색 콘솔


### 코드/원리 
---
- 밑의 줄은 search.py 코드입니다.
 - word_list.json을 updater.py 에서 다운받아옴.
 - word_list.json에서 콘솔에 입력한 글자로 시작하는 단어를 찾음.
 - 프린트 함

밑 줄은 코드 입니다.

    import json
    
    # ----------------------- # 
    #       단어 읽어오기
    # ----------------------- # 
    try:
        with open('word_list.json', 'r', encoding='utf-8') as json_file:
            word_list = json.load(json_file)
    except FileNotFoundError:
        print("word_list.json 파일이 존재하지 않습니다.")
        exit()
    except json.JSONDecodeError:
        print("word_list.json 파일의 형식이 잘못되었습니다. ")
        exit()

    # ----------------------- # 
    #    단어 찾기 프린트하기
    # ----------------------- # 
    while True:
        input_char = input("한글자를 입력해주세요: ")
        if input_char.lower() == 'exit':
            break
        matching_words = [word for word in word_list if word.startswith(input_char)]
        if matching_words:
            print(f"'{input_char}'으로 시작하는 단어들은 다음과 같습니다: {matching_words}")
        else:
            print(f"'{input_char}'으로 시작하는 단어를 찾지 못했습니다.")
