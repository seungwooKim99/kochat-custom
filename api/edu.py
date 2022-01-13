class EduAnswerer():

    def request(self, keyword: str):
        try:
            return self.request_debug(keyword)
        except Exception as e:
            print(e)
            return "죄송합니다. 오류가 발생했어요."

    def request_debug(self, keyword: str):
        if "파이썬" in keyword:
            answer = "파이썬은 1991년 네덜란드계 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, 플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑 대화형 언어입니다."
        elif ("가상환경" in keyword) or ("가상" in keyword):
            answer = "가상환경(Virtual Environments)이란 자신이 원하는 Python 환경을 구축하기 위해 필요한 모듈만 담아 놓는 바구니입니다."
        elif "클래스" in keyword:
            answer = "클래스(class)는 객체 지향 프로그래밍(OOP)에서 특정 객체를 생성하기 위해 변수와 메소드를 정의하는 일종의 틀입니다. 객체를 정의 하기 위한 상태(멤버변수)와 메서드(함수)로 구성돼요."
        else:
            answer = "죄송합니다. 무슨 말인지 이해하지 못했어요. 제게 말씀해주신 키워드는 {0} 입니다.".format(keyword)
        return answer