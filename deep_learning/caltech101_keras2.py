import caltech101_keras

# 예측하기
pre = model.predict(x_test)

# 예측 결과 테스트하기
for i, v in enumerate(pre) :
    pre_ans = v.argmax()      # 예측한 레이블
    ans = y_test[i].argmax()  # 정답 레이블
    dat = x_test[i]           # 이미지 데이터

    if ans == pre_ans :
        continue
    
    # 예측이 틀리면 무엇이 틀렸는지 출력하기
    print('[NG]', categories[pre_ans], "!=", categories[ans])
    print(v)

    # 이미지 출력하기
    fname = 'image/error/' + str(i) + '_' + categories[pre_ans] + \
        "_ne_" + categories[ans] + ".PNG"
    dat *= 256
    img = Image.fromarray( np.unit8(dat) )
    img.save(fname)
