import gradio as gr

def add(num1, num2):
    return num1 + num2

# interface를 만들면 clear, submit, flag 버튼을 자동으로 만들어준다.
# flag: 사용자의 입력과 출력을 기록하여 문제상황이나 유용한 사례를 저장, 분석할 수 있다.
interface = gr.Interface(
    fn = add,
    inputs = ['number', 'number'],
    outputs = 'number',
    title = '계산기',
    description = '숫자 두 개를 입력하세요.',
    flagging_mode="never" # flag를 하지 않음
)

interface.launch()