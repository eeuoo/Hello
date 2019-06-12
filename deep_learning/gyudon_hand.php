<?php
$self = 'gyudon_hand.php' ;
$base_dir = dirname(__FILE__)."/data";
$unkown_dir = "gyudon" ;
$dirs = array(
    '일반 규동' => 'normal',
    '생강 규동' => 'beni',
    '양파 규동' => 'negi',
    '치즈 규동' => 'cheese',
    '김치 규동' => 'kimchi',
    '기타' => 'other',
);

// 필요한 폴더 생성하기
foreach ($dirs as $key => $dir) {
    $path = $base_dir.'/$dir' ;
    if (!file_exists($path)) {
        mkdir($path);
        chmod($path, 0777);
    }
}

// 분류하거나 입력 양식 제공하기
$m = isset($_GET['m']) ? $_GET['m'] : '' ;
if ($m == 'mv') { // 분류하기
    $target = $_GET['target']; // 요청 매개변수 추출하기
    $to = $_GET['to'];
    $path = $base_dir.'/$unkown_dir/$target';
    // 요청 매개변수 확인하기
    if ($target == '') {
        echo 'error....';
        exit;
    }
    if (!file_exists($path)){
        echo "<a herf='$self'>already ...</a>";
        exit;
    }
    if (!file_exists('$base_dir/$to')) {
        echo 'system error : no dir $to';
        exit;
    }
}

// 파일 이동 (복사한 뒤에 제거하기)
$path_to = '$base_dir/$to/$target';
copy($path, $path_to);
if (file_exists($path_to)) {
    unlink($path);
}else {
    echo 'Sorry, could not move.';
    exit ;
}