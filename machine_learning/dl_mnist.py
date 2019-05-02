import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("mnist/", one_hot=True)
print(mnist.train.images)
print(mnist.train.labels)
print("length=", len(mnist.train.images), len(mnist.test.images))

# 크기 정의
pixels = 28 * 28
nums = 10   # 0~9

# 가중치와 bias를 변수(Variable)화
x = tf.placeholder(tf.float32, shape=(None, pixels), name="x")        # image data (None: 가변)
y_ = tf.placeholder(tf.float32, shape=(None, nums), name="y_")        # label


def weight_variable(name, shape):
    W_init = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(W_init, name="W_"+name)


def bias_variable(name, size):
    b_init = tf.constant(0.1, shape=[size])
    return tf.Variable(b_init, name="b_" + name)


def conv2d(x, W):
    # 1 X 1 이므로 크기 동일
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool(x):
    # 2 X 2 kernel size (28 X 28 => 14 X 14 => 7 X 7 => 4 X 4)  즉, 50%만 sampling하겠다!   (cf. mean_pool)
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')


# Convolution(합성곱) Layer L1 (cf. L1 ~ Ln)
with tf.name_scope('conv1') as scope:
    # 5 X 5 필터, input=1(흑백), output=32 : 이미지 1개를 32개의 필터(출력)로!
    W_conv1 = weight_variable('conv1', [5, 5, 1, 32])
    b_conv1 = bias_variable('conv1', 32)
    x_image = tf.reshape(x, [-1, 28, 28, 1])     # -1(n개)의 28 X 28 X 1 이미지
    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)      # cf. tf.sigmoid

# Max-Pooling Layer1
with tf.name_scope('pool1') as scope:
    h_pool1 = max_pool(h_conv1)

# Convolution(합성곱) Layer L2
with tf.name_scope('conv2') as scope:
    # 5 X 5 filter, 32개 입력, 64개 필터(출력)
    W_conv2 = weight_variable('conv2', [5, 5, 32, 64])
    b_conv2 = bias_variable('conv2', 64)
    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)

# Max-Pooling Layer2
with tf.name_scope('pool2') as scope:
    h_pool2 = max_pool(h_conv2)

# fully-connect (1차원으로 펼치기)
with tf.name_scope('fully_connected') as scope:
    W_fc = weight_variable('fc', [7 * 7 * 64, 1024])  # 7 = 28 % 2 % 2  (2개의 Hidden Layer)
    b_fc = bias_variable('fc', 1024)

    # -1(n개)를 1차원 list로 펼치기(3,136)
    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    h_fc = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc) + b_fc)

# dropout (과잉적합 막기, fast-forward, split-merge, RNN)
with tf.name_scope('dropout') as scope:
    keep_prob = tf.placeholder(tf.float32)          # dropout rate
    h_fc_drop = tf.nn.dropout(h_fc, keep_prob)

# output
with tf.name_scope('readout') as scope:
    W_fc2 = weight_variable('fc2', [1024, 10])   # 0 ~ 9인 10개 결과
    b_fc2 = bias_variable('fc2', 10)
    y_conv = tf.nn.softmax(tf.matmul(h_fc_drop, W_fc2) + b_fc2)    # softmax regression

# loss op
with tf.name_scope('loss') as scope:
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))   # Fit: 교차엔트로피 최소화

# training 연산자(op) 생성
with tf.name_scope('training') as scope:
    optimizer = tf.train.AdamOptimizer(1e-4)           # 확률적 경사하강법
    train_step = optimizer.minimize(cross_entropy)   

# 평가(test) 연산자(op) 생성
with tf.name_scope('predict') as scope:
    predict_step = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))  # label과 같으면 1, 다르면 0
    accuracy_step = tf.reduce_mean(tf.cast(predict_step, tf.float32))  # fit

# image data와 label(결과)을 placeholder화
def set_feed(images, labels, prob):
    return {x: images, y_: labels, keep_prob: prob}    # prob:  training(0.5 or 0.7), test(1)


# run
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    test_fd = set_feed(mnist.test.images, mnist.test.labels, 1) 
    for step in range(10000):
        batch = mnist.train.next_batch(50)
        fd = set_feed(batch[0], batch[1], 0.5)  # test: 0.5
        _, loss = sess.run([train_step, cross_entropy], feed_dict=fd)
        if step % 10 == 0:
            acc = sess.run(accuracy_step, feed_dict=test_fd)
            print("step=", step, ", loss=", loss, ", acc=", acc)

    acc = sess.run(accuracy_step, feed_dict=test_fd)
    print("정답률=", acc)
