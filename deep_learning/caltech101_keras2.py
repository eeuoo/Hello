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
    fname = './data/error/' + str(i) + '_' + categories[pre_ans] + \
        "_ne_" + categories[ans] + ".PNG"
    dat *= 256
    img = Image.fromarray( np.unit8(dat) )
    img.save(fname)

hdf5_file = './data/5obj_model.hdf5'

if os.path.existx(hdf5_file) :
    # 기존에 학습된 모델 읽어 들이기
    model.load_weights(hdf5_file)

else :
    # 학습한 모델을 파일로 저장하기
    model.fit(x_train, y_train, batch_size = 32, nb_epoch = 50)
    model.save_weights(hdf5_file)


