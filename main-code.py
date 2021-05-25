# 1. 완료됨?이라는 질문을 물어봄
# 2-1. y라는 대답이면 값 a=1 을 저장
# 2-2. 다신 완료됨?이라는 질문을 물어봄
# 3-1. n라는 대답이어도 값 a=0 을 저장
# 3-2. 다시 완료됨?이라는 질문을 물어봄
# 4. 질문을 반복해서 물어봄
# 5. 값의 합이 6이 되면 멈추고 "완료됨"을 프린트


def append(number, number_list = []):
    number_list.append(number)
    return number_list

def the_question():
    question = input("          조원 모두 완료 했나요? [y/n]")
    # for i in question:
    if question == "y":
        # print("수고하셨습니다. 다른 조가 마칠 때까지 기다려주세요.")
        return 1
    elif question == "n":
        print("             그럼 나와서 누르지 말고 빨리 하세요!")
        return None
    else:
        print("             음...그 버튼은 누를 수 없습니다.")
        return None



def mix():
    while True:
        number = the_question()
        a = append(number)
        a = list(filter(lambda x: x != None, a))
        b = sum(a)%6
        print("             ***<MPM 프로토콜> 상황 보고: <" + str(b) + "/6> 완료.")
        if len(a) != 0 and len(a)%6 == 0:
            print("6조 모두 완료하였습니다.")
            break


def reset():
    question = input("<MPM 프로토콜>을 재실행 하시겠습니까? [y/n]")
    if question == "y":
        print("     <MPM 프로토콜>을 재시작합니다.")
        mix()
        reset()
    elif question == "n":
        print("     <MPM 프로토콜>을 종료합니다. 반장 최진우한테 보고해주세요.")
    else:
        print("     입력 불가입니다. y 또는 n을 눌러주세요.")
        reset()



def repeat():
    question = input("Mission Progress Monitoring Protocol(MPM 프로토콜)을 실행하시겠습니까? [y/n]")
    if question == "y":
        print("     <MPM 프로토콜>을 시작합니다.")
        mix()
        reset()
    elif question == "n":
        print("     그럼 반장 최진우한테 알아서 보고하세요.")
    else:
        print("     입력 불가입니다. y 또는 n을 눌러주세요.")
        repeat()

repeat()
