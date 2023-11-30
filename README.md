# 끝말잇기 한방단어 검색 Python

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
