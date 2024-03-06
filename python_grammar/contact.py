contact = {}

while True:
    print('------ 전화번호부 프로그램 ------')
    print('1.추가   2.보기    3.검색   4.수정   5.삭제    9.종료')

    menu = int(input('메뉴를 선택해주세요(숫자 only)'))

    if menu == 1:
        print('연락처를 추가합니다.')
        new_name = input('이름 : ')
        new_tel = input('전화번호 : ')
        print(new_name, new_tel)
        # contact[new_name] = new_tel # 덮어쓰기
        contact.setdefault(new_name, new_tel)

    elif menu == 2:
        print('연락처를 조회합니다.')
        # print(contact)
        # print('='*10)
        for name, tel in contact.items():
            print(name, ":", tel)

    elif menu == 3:
        print('연락처를 검색합니다.')
        search_name = input('검색 이름: ')
        # print(contact[search_name])
        print(contact.get(search_name, '없는 연락처입니다.'))

    elif menu == 4:
        print('연락처를 수정합니다.')
        mod_name = input('수정 이름 : ') # 연락처에 있을 경우에만 새전화번호를 묻는 것이.
        if mod_name in contact:
            mod_tel = input('새 전화번호 : ')
            contact[mod_name] = mod_tel
        else :
            print('등록되지 않은 이름입니다.')

    elif menu == 5:
        print('연락처를 삭제합니다.')
        del_name = input('삭제 이름 : ')
        if del_name in contact:
            del contact[del_name]
        else :
            print('등록되지 않은 이름입니다.')

    elif menu == 9:
        print('프로그램을 종료합니다.') 
        break

    else :
        print('잘못된 입력입니다.')