# raise를 이용한 예외의 발생
def get_ans(ans) :
  if ans in ['예', '아니오'] :
    print('정상입니다.')
  else :
    raise ValueError('입력을 확인하세요.')

while True :
  try :
    ans = input('예/아니오 중 하나를 입력하세요 : ')
    get_ans(ans)
    break
  except Exception as e :
    print('error : ', e)