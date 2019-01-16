<script charset="UTF-8" src="https://stdpay.inicis.com/stdjs/INIStdPay.js" type="text/javascript"></script>
<link href="http://tkfile.yes24.com/img/favicon.ico?ver=150825a" rel="shortcut icon" type="image/x-icon"/>
<script type="text/javascript">
        var jgIdPerf = '32098';
        var now = new Date();
        var txtDate = now.getFullYear() + jsf_def_PadLeft(now.getMonth() + 1, 2) + jsf_def_PadLeft(now.getDate(), 2) + jsf_def_PadLeft(now.getHours(), 2) + jsf_def_PadLeft(now.getMinutes(), 2);



    </script>
<!-- 예매 스크립트 로드 -->
<script src="/Pages/Perf/Sale/Scripts/ps_gobalVariables.js?v3=844" type="text/javascript"></script>
<!-- 예매 스크립트 로드 -->
<script src="/Pages/Perf/Sale/Scripts/ps_perfCalendar.js?v3=844" type="text/javascript"></script>
<!-- 예매 스크립트 로드 -->
<script src="/Pages/Perf/Sale/Scripts/ps_divControls.js?v3=844" type="text/javascript"></script>
<!-- 예매 스크립트 로드 -->
<script src="/Pages/Perf/Sale/Scripts/ps_asyncBooking.js?v3=844" type="text/javascript"></script>
<!-- 예매 스크립트 로드 -->
<script src="/Pages/Perf/Sale/Scripts/ps_ticketSale.js?v3=844" type="text/javascript"></script>
<!-- 예매 스크립트 로드 -->
<!--
            ※ 주의!!!
            * 웹SITE 가 https를 이용하면 https://plugin.inicis.com/pay61_secunissl_cross.js 사용
            * 웹SITE 가 Unicode(UTF-8)를 이용하면 http://plugin.inicis.com/pay61_secuni_cross.js 사용
            * 웹SITE 가 https, unicode를 이용하면 https://plugin.inicis.com/pay61_secunissl_cross.js 사용
        -->
</head>
<body>
<div id="progressBar" style="width:300px;display:none;"></div>
<script type="text/javascript">
            $j("#progressBar").jry_home_ShowProgressBar({ "state": "start" });
        </script>
<div id="dialogPayProgress" style="display:none;"></div>
<div id="dialogAlert" style="display:none;"></div><div id="dialogConfirm" style="display:none;"></div><div id="dialogPopup" style="display:none;"></div>
<!-- UI 영역 START -->
<div id="warp">
<div id="all" style="display: block;">
<!--상단메뉴 -->
<div class="header" id="header">
<h1><img alt="YES24.com" src="http://tkfile.yes24.com/img/perfsale/h1_tit.gif"/></h1>
<ul class="gnb">
<li class="m01"><span>관람일/회차</span></li>
<li class="m02"><span>좌석선택</span></li>
<li class="m03"><span>할인/쿠폰</span></li>
<li class="m04"><span>수령방법</span></li>
<li class="m05"><span>결제방법</span></li>
</ul>
</div>
<!--//상단메뉴 -->
<!-- 내용컨탠츠 -->
<div class="container" id="ContentsArea">
<!-- 제 1 단계 : 관람일/회차 -->
<div id="step01">
<!-- 관람일선택 -->
<div class="step01_date" id="step01_date">
<h2><img alt="관람일선택" src="http://tkfile.yes24.com/img/perfsale/h2_tit01.gif"/><span><img alt="" src="http://tkfile.yes24.com/img/perfsale/icon_nt.gif"/></span></h2>
<div class="calendar" id="calendar">
</div>
</div>
<!-- //관람일선택 -->
<!--회차선택 -->
<div class="step01_time" id="step01_time">
<div style="display: none;">
<p><img alt="관람일을 선택해주세요" src="http://tkfile.yes24.com/img/perfsale/img_select.gif"/></p>
</div>
<div style="display: block;">
<h2><img alt="회차선택" src="http://tkfile.yes24.com/img/perfsale/h2_tit02.gif"/><span><img alt="" src="http://tkfile.yes24.com/img/perfsale/icon_nt.gif"/></span></h2>
<div class="choie_select">
<div class="select_day">
<em class="tit">선택날짜</em><span> </span>
</div>
<div class="number">
<em class="tit">회차선택</em>
<ul id="ulTime"></ul>
<div class="point" style="display: none;"><img alt="YES포인트" src="http://tkfile.yes24.com/img/common/btn_p02.gif"/><span><em>적립 제외 회차</em></span></div>
</div>
<div class="seat">
<em class="tit">좌석등급/잔여석</em>
<ul class="hi" id="ulSeatSpace"></ul>
</div>
<div class="btn">
<div class="fr">
<img alt="좌석선택" class="dcursor" id="btnSeatSelect" onclick="fdc_ChoiceSeat();" src="http://tkfile.yes24.com/img/perfsale/btn_seat.gif"/>
</div>
</div>
</div>
</div>
</div>
<!-- //회차선택 -->
<!-- 공연안내 -->
<div class="step01_notice" id="step01_notice">
<h3><img alt="유의사항" src="http://tkfile.yes24.com/img/perfsale/h3_tit_notice.gif"/></h3>
<div id="guideview"></div>
<!-- 공연안내 미등록시 보여줄 Default 문구 -->
<div id="guideview_default" style="display: none;">
<ul>
<li>- 할인은 자동선택 되지 않으니, <u>적용 받고자 하는 할인이 있는 경우 직접 선택</u>해주시기 바랍니다.</li>
<li>- 장애인, 국가유공자, 학생 할인 등 증빙서류가 필요한 경우 현장수령만 가능하며, <u>현장에서 증빙서류 미지참 시 차액 지불</u>하셔야 합니다.</li>
<li>- <u>쿠폰을 사용하거나 복합결제를 한 경우 부분취소가 불가</u>합니다. 고객센터로 문의해주시기 바랍니다.</li>
<li>- <u>관람 당일 공연 예매 시에는 변경/취소/환불이 불가</u>합니다.</li>
<li>- 경우에 따라 ATM 기기에서 가상계좌 입금이 안 될 수 있으니 가급적 인터넷/폰뱅킹 등을 이용해주시기 바랍니다.</li>
<li>- 예매 취소 시 <u>예매수수료는 예매 당일 밤 12시 이전까지 환불되며, 그 이후 기간에는 환불되지 않습니다.</u></li>
<li>- 예매 취소 시점에 따라 취소수수료가 부과될 수 있습니다. 예매 후 취소마감시간과 함께 취소수수료를 꼭 확인해주시기 바랍니다.</li>
</ul>
</div>
</div>
<!-- //공연안내 -->
</div>
<!-- //제 1 단계 : 관람일/회차 -->
<!-- 제 3 단계 : 할인/쿠폰 -->
<div id="step03" style="display: none;">
<!-- 할인선택 -->
<div class="step03_promotion">
<h2><img alt="할인선택" src="http://tkfile.yes24.com/img/perfsale/h2_tit03.gif"/><span><img alt="" src="http://tkfile.yes24.com/img/perfsale/icon_nt.gif"/></span></h2>
<div class="disc_select">
<div class="select_seat">
<em class="tit">등급선택</em>
<span id="spanPromotionSeat">
<input name="" type="radio" value=""/><label>VIP석</label>
<input name="" type="radio" value=""/><label class="red">R석</label>
<input name="" type="radio" value=""/><label>A석</label>
</span>
</div>
<div class="scroll" id="divPromotionList" style="height:228px !important"></div>
</div>
</div>
<!-- //할인선택 -->
<!-- 쿠폰선택 -->
<div class="step03_coupon">
<h2><img alt="쿠폰선택" src="http://tkfile.yes24.com/img/perfsale/h2_tit04.gif"/><span><img alt="" src="http://tkfile.yes24.com/img/perfsale/icon_nt.gif"/></span></h2>
<div class="sale_select">
<div class="select_coupon tr" style="margin-bottom:5px !important">
<a class="dcursor" onclick="fdc_PopupCouponRegister();"><img alt="쿠폰등록" src="http://tkfile.yes24.com/img/perfsale/btn_coupon2.gif"/></a>
</div>
<div class="scroll" id="divCouponList" style="height:106px !important"></div>
<p><strong class="red">주의사항) </strong><span>할인은 자동선택 되지 않으니, <strong class="red">적용 받고자 하는 할인이 있는 경우 직접 선택</strong>해주시기 바랍니다. <!--1) 쿠폰은 중복사용이 불가능합니다 (단, “중복사용가능” 표기 쿠폰은 쿠폰간 중복사용이 가능합니다)//--></span></p>
</div>
</div>
<!-- //쿠폰선택 -->
</div>
<!-- //제 3 단계 : 할인/쿠폰 -->
<!-- 제 4 단계 : 수령방법 -->
<div class="step04" id="step04" style="display: none;">
<h2><img alt="수령방법" src="http://tkfile.yes24.com/img/perfsale/h2_tit05.gif"/><span><img alt="" src="http://tkfile.yes24.com/img/perfsale/icon_nt.gif"/></span></h2>
<div class="receipt_select">
<!-- 수령방법선택 -->
<div class="select_seat">
<em class="tit">수령방법선택</em>
<span id="deliveryPos">
<input name="" type="radio" value=""/><label>현장수령</label>
<input name="" type="radio" value=""/><label class="red">배송</label>
</span>
</div>
<!-- //수령방법 -->
<!-- 주문자확인 정보 -->
<div id="step04_OrdererInfo">
<h4>주문자확인</h4>
<ul>
<li><em>이름</em><input class="imekor" id="ordererUserName" maxlength="50" readonly="readonly" style="width: 110px;" type="text"/></li>
<li><em>

                                      긴급연락처

                                    </em>
<input class="imedisable" id="ordererMobile1" maxlength="3" style="width: 30px;" type="text"/>
                                        -
                                        <input class="imedisable" id="ordererMobile2" maxlength="4" style="width: 50px;" type="text"/>
                                        -
                                        <input class="imedisable" id="ordererMobile3" maxlength="4" style="width: 50px;" type="text"/>
</li>
<li><em>e-mail</em>
<input class="imedisable" id="ordererMailH" maxlength="50" onclick="fdc_emailClick()" readonly="readonly" style="width: 110px;" type="text"/>
                                        @
                                        <input class="imedisable" id="ordererMailD" maxlength="50" onclick="fdc_emailClick()" readonly="readonly" style="width: 110px;" type="text"/>
</li>
</ul>
</div>
<!-- //주문자확인 정보 -->
<!-- 배송지 정보 -->
<div class="add_info" id="step04_DeliveryInfo">
<h4>배송지정보<span>2016년 8월 1일부터 5자리 우편번호 사용이 의무화됩니다.<br/>도로명주소+5자리 우편번호로 등록하셔서 티켓 배송에 문제가 없도록 협조부탁드립니다.</span></h4>
<ul>
<li><em>받으시는분</em>
<input class="imekor" id="deliveryUserName" maxlength="50" style="width: 110px;" type="text"/>
<span>
<input id="deliveryInfoType0" name="deliveryInfoType" onclick="fdc_DisplayUserInfo(this);" type="radio" value="0"/><label>주문자정보와동일</label>
<input id="deliveryInfoType1" name="deliveryInfoType" onclick="fdc_DisplayUserInfo(this);" type="radio" value="1"/><label>최근배송지<a id="btnRecentAddress"><img alt="더보기" src="http://tkfile.yes24.com/img/perfsale/btn_more.gif"/></a></label>
<input id="deliveryInfoType2" name="deliveryInfoType" onclick="fdc_DisplayUserInfo(this);" type="radio" value="2"/><label>새로입력</label>
</span></li>
<li><em>휴대폰/전화</em>
<input class="imedisable" id="deliveryMobile1" maxlength="3" style="width: 30px;" type="text"/>
                                        -
                                        <input class="imedisable" id="deliveryMobile2" maxlength="4" style="width: 50px;" type="text"/>
                                        -
                                        <input class="imedisable" id="deliveryMobile3" maxlength="4" style="width: 50px;" type="text"/>
</li>
<li><em>주소</em>
<input class="imedisable" id="deliveryZipCode1" maxlength="6" style="width: 80px;" type="text"/> -
                                        <input class="imekor" id="deliveryAddress1" maxlength="200" style="width: 240px;" type="text"/>
<a id="btnSearchAddress"><img alt="우편번호검색" src="http://tkfile.yes24.com/img/perfsale/btn_zip.gif"/></a>
</li>
<li id="lideliveryAddress2"><em>상세주소</em>
<input class="imekor" id="deliveryAddress2" maxlength="100" style="width: 330px;" type="text"/>
</li>
</ul>
</div>
<!-- //배송지 정보 -->
<!-- 주의사항 -->
<div class="caution" id="step04_DeliveryCaution">
<h5>주의사항 <em style="font-weight:normal;">* 부정확한 정보 입력으로 인한 문제 발생 시 예스24는 책임을 지지 않습니다.</em></h5>
<ul>
<li>1)<span class="red"> 배송 선택 시 티켓 수령자의 배송지 정보를 정확히 입력해주시기 바랍니다.</span></li>
<li>2)<span class="red"> 티켓은 유가증권으로 본인에게 직접 전달해야하며, 분실된 티켓은 재발권 되지 않습니다.</span></li>
<li>3)<span class="red"> 일괄배송의 경우 정해진 날짜에 티켓 배송이 시작되며, 주소 수정은 일괄배송일 2일 전까지 가능합니다.</span></li>
<li>4)<span class="red"> 예매 티켓 배송은 예매완료일, 혹은 일괄배송일로부터 4~5일(영업일 기준) 이내 수령 가능합니다.</span> </li>
<li>5) 긴급연락처는 공연 취소와 같은 유사 시 안내 받으실 연락처이므로 정확히 입력해주시기 바랍니다.</li>
<li>6) 이메일 정보 미 입력 시 예매 관련 안내 메일을 받을 수 없으니 이메일 받기를 원하시는 경우 마이페이지에서<br>   회원정보를 수정해주시기 바랍니다.</br></li>
</ul>
</div>
<!-- //주의사항 -->
<div id="step04_OverseasDeliveryInfo" style="display:none">
<h4>Information for Delivery <span style="font-weight: normal; color: #888">Please fill all the element by English</span></h4>
<ul>
<li><em>Area</em>
<select id="selOverseasDeliveryArea" name="" onchange="fdc_OverseasDeliveryChange(this)" style="width: 116px;">
</select>
</li>
<li><em>Country</em>
<select id="selOverseasDeliveryCountry" name="" style="width: 116px;">
</select>
</li>
<li><em>Name</em><input id="overseasDeliveryName" style="width: 110px;" type="text"/></li>
<li><em>Tel or Mobile</em>
<input class="imedisable" id="overseasDeliveryMobile1" maxlength="3" style="width: 30px;" type="text"/>
                                        -
                                        <input class="imedisable" id="overseasDeliveryMobile2" maxlength="4" style="width: 30px;" type="text"/>
                                        -
                                        <input class="imedisable" id="overseasDeliveryMobile3" maxlength="4" style="width: 40px;" type="text"/>
                                        -
                                        <input class="imedisable" id="overseasDeliveryMobile4" maxlength="4" style="width: 40px;" type="text"/>
<span>Please fill with the Country code (ex)+82-010-000-0000</span> </li>
<li><em>Zip code</em>
<input class="imedisable" id="overseasDeliveryZipcode" maxlength="10" style="width: 110px;" type="text"/>
</li>
<li><em>City</em>
<input id="overseasDeliveryCity" maxlength="30" style="width: 170px;" type="text"/>
</li>
<li><em>Address</em>
<input id="overseasDeliveryAddress1" maxlength="130" style="width: 500px;" type="text"/>
</li>
</ul>
</div>
<div class="caution" id="step04_OverseasDeliveryCaution" style="display:none">
<h5>Notice <em style="font-weight: normal;">* YES24 won’t be responsible for problems occur due to incorrect information entered.</em></h5>
<ul>
<li>1) Please fill correct recipient information when you choose the overseas delivery.</li>
<li>2) In the case of bulk delivery, these tickets will be start at fixed dates and modification of address is
                                        <br/>
                                          possible until 2 days before the starting date.</li>
</ul>
</div>
<!-- //주의사항 -->
</div>
</div>
<!-- //제 4 단계 : 수령방법 -->
<!-- 제 5 단계 : 결제방법 -->
<div class="step05" id="step05" style="display: none;">
<h2><img alt="결제방법" src="http://tkfile.yes24.com/img/perfsale/h2_tit06.gif"/><span><img alt="" src="http://tkfile.yes24.com/img/perfsale/icon_nt.gif"/></span></h2>
<div class="receipt_select receipt_pt0">
<!-- 결제수단 & 결제방법선택 -->
<div class="receipt_scroll receipt_hsize">
<ul class="mb">
<!-- YES머니 -->
<li id="liYesMoney">
<em>YES머니</em>
<span class="cont"><input id="txtYesMoney" onchange="fdc_CheckYesMoney();" style="width: 120px;" type="text"/>원</span>
<span><input id="cbxYesMoney" onclick="fdc_UseFullYesMoney();" type="checkbox"/>전액사용 (총 <strong id="lblYesMoney"> </strong>원) </span>
<!-- YES포인트 -->
<span id="liYesPoint">
<span>/ YES포인트 <strong id="lblYesPoint"> </strong> 원</span>
<span>
<a id="imgExchangePoint" onclick="fdc_PopupExchangePoint()" style="cursor:pointer;cursor:hand;">
<img alt="YES머니로 환전" src="http://tkfile.yes24.com/img/perfsale/btn_yes01.gif"/></a></span>
</span>
<!-- //YES포인트 -->
</li>
<!-- //YES머니 -->
<!-- 예치금 -->
<li id="liYesDeposit">
<em>예치금</em>
<span class="cont"><input id="txtYesDeposit" onchange="fdc_CheckYesDeposit();" style="width: 120px;" type="text"/>원</span>
<span><input id="cbxYesDeposit" onclick="fdc_UseFullYesDeposit();" type="checkbox"/>전액사용 (총 <strong id="lblYesDeposit"> </strong>원) </span>
</li>
<!-- //예치금 -->
<!-- YES24상품권 -->
<li id="liYesGift">
<em>YES24상품권</em>
<span class="cont"><input id="txtYesGift" onchange="fdc_CheckYesGift();" style="width: 120px;" type="text" usedgiftinfo=""/>원</span>
<span><a id="imgYesGiftUse" onclick="fdc_PopupYesGiftUse()" style="cursor:pointer;cursor:hand;"><img alt="사용하기" src="http://tkfile.yes24.com/img/perfsale/btn_use.gif"/></a> (총 <strong id="lblYesGiftAmt"> </strong>원 / 사용가능 <strong id="lblYesGiftCnt"> </strong>장) </span>
</li>
<!-- //YES24상품권 -->
<!-- 외부상품권 -->
<!-- //외부상품권 -->
<!-- 공연예매권 -->
<li class="d_line" id="liGiftTicket">
<em>공연예매권</em>
<span class="con">
                                            사용가능 예매권[총 <strong class="blu" id="lblGiftTicketUsable"> </strong>장]
                                            <a class="dcursor" id="imgGiftTicketRegUse" onclick="fdc_PopupGiftTicketRegUse()"><img alt="예매권 번호 등록/사용하기" src="http://tkfile.yes24.com/img/perfsale/btn_yes02.gif"/></a>
</span>
<div id="divGiftTicketUsedView" style="display:none"><span class="ticket fst">사용하신 예매권이 없습니다.</span></div>
</li>
<!-- //공연예매권 -->
<!-- 베네피아포인트 -->
<li class="d_line" id="liBenepiaPoint" style="display: none;">
<em>베네피아포인트</em>
<span class="cont"><input disabled="disabled" id="txtBenepiaPoint" style="width: 120px;" type="text" usedbenepiainfo=""/>원</span>
<span><input id="cbxBenepiaPoint" onclick="fdc_UseBenepiaPoint();" type="checkbox"/> 사용</span>
</li>
<!-- //베네피아포인트 -->
<!-- OK 캐쉬백 적립 -->
<li class="d_line" id="liOKCashbag" style="display: none;">
<em>OK 캐쉬백 적립</em>
<span class="cont" style="width:235px;">
<input class="imedisable" id="txtOKCashbagCardNo1" maxlength="4" style="width: 40px;" type="text"/>
                                            -
                                            <input class="imedisable" id="txtOKCashbagCardNo2" maxlength="4" style="width: 40px;" type="text"/>
                                            -
                                            <input class="imedisable" id="txtOKCashbagCardNo3" maxlength="4" style="width: 40px;" type="text"/>
                                            -
                                            <input class="imedisable" id="txtOKCashbagCardNo4" maxlength="4" style="width: 40px;" type="text"/>
</span>
<input id="chkOKCashBAgree" type="checkbox"/><label>OK캐쉬백 정보 제공 동의 <a href="javascript:fdc_PopOkCashBAgree()" style="vertical-align:middle;">[상세보기]</a></label>
</li>
<!-- //OK 캐쉬백 적립 -->
<!-- 결제방법선택 -->
<li class="d_line"><em class="blu">결제방법선택</em>
<div class="con conpd">
<ul id="paymethodPos"></ul>
<a class="more" href="#" style="display:none;"><img alt="신용카드 및 무통장입급안내" src="http://tkfile.yes24.com/img/perfsale/btn_infor03.gif"/></a>
</div>
</li>
<li class="d_line" id="liLiveRefundinfo" style="display:none;">
<em class="blu">환불계좌입력</em>
<div class="con">
<ul>
<li><select disabled="disabled" id="selLiveRefundBank" style="height:20px;">
<option selected="" value="0">환불은행 선택</option>
</select>
</li>
<li><input disabled="disabled" id="txtLiveRefundAccount" maxlength="14" style="width:120px;" type="text"/></li>
<li>예금주명 <input disabled="disabled" id="txtLiveRefundUserName" maxlength="50" style="width:120px;" type="text"/></li>
</ul>
<div class="conpd">* 함께 볼 사람이 목표에 도달하지 못 할 경우 예스24 라이브는 취소되며 전액 환불 됩니다.</div>
</div>
</li>
<li class="d_line">
<em class="blu">자동주문방지</em>
<div class="con">
<img id="captchaImg" src="" width="180px"/>
<div style="position:absolute;left:190px;top:15px;">
<a href="javascript:initCaptcha();"><img alt="새로고침" src="http://tkfile.yes24.com/img/common/ic_refresh.png" width="12px"/>새로고침</a>
<input id="captchaText" name="captchaText" style="display:block; width:160px;height:22px;margin-top:5px; padding:3px;" type="text"/>
<input id="captchaKey" name="captchaKey" type="hidden"/>
</div>
</div>
</li>
<!-- //결제방법선택 -->
</ul>
<!-- 결제수단 & 결제방법선택 -->
<!-- 취소수수료 안내 및 약관동의 -->
<div class="caution bgbrn">
<!--h5>취소수수료 안내 및 이용 약관</h5-->
<div class="box">
<em>취소 가능 마감 시간 : </em><span class="red" id="lblCancelTimeInfo"> </span>
</div>
<table class="boardListTypeB tb_w">
<colgroup>
<col align="center" width="33%"/>
<col align="center" width="38%"/>
<col width="*"/>
</colgroup>
<thead>
<tr>
<th>내용</th>
<th>취소수수료</th>
<th>비고</th>
</tr>
</thead>
<tbody>
<tr>
<td>예매 후 7일 이내</td>
<td>없음</td>
<td class="bl_p alignLeft" rowspan="5">- 취소 시 예매수수료는 예매 당일 밤 12시 이전까지만 환불됩니다. <br>
                                    - 예매 후 7일 이내라도 취소시점이 관람일로부터 10일 이내라면 그에 해당하는 취소수수료가 부과됩니다.  <br/>
                                    - 관람 당일 취소 가능 상품의 경우 관람 당일 취소 시 티켓금액의 90%가 취소수수수료로 부과됩니다.
                                    </br></td>
</tr>
<tr>
<td>예매 후 8일 ~ 관람일 10일 전까지</td>
<td>뮤지컬, 콘서트, 클래식 등: <span class="red">장당 4,000원</span> /<br/> 연극, 전시 등: <span class="red">장당 2,000원</span> <br>(단, 티켓 금액의 10% 이내)</br></td>
</tr>
<tr>
<td>관람일 9일 전 ~ 관람일 7일 전까지</td>
<td>티켓금액의 <em class="red">10%</em></td>
</tr>
<tr>
<td>관람일 6일 전 ~ 관람일 3일 전까지</td>
<td>티켓금액의 <em class="red">20%</em></td>
</tr>
<tr>
<td>관람일 2일 전 ~ 관람일 1일 전까지</td>
<td>티켓금액의 <em class="red">30%</em></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
<!-- //취소수수료 안내 및 약관동의 -->
<span class="chkbox">
<input id="cbxCancelFeeAgree" type="checkbox"/><label>취소수수료 및 취소기한을 확인하였으며, 동의합니다.</label>
<input id="chkinfoAgree" type="checkbox"/><label>제3자 정보제공 내용에 동의합니다. <a href="javascript:fdc_PopupSaleAgree('32098')">[상세보기]</a></label>
</span>
</div>
<!-- //제 5 단계 : 결제방법 -->
</div>
<!--// 내용컨탠츠 -->
<!-- 상황판 -->
<div id="StateBoard">
<div class="result">
<div class="title" id="perfboard">
<p><img alt="" height="98" src="http://tkfile.yes24.com/img/common/noimg.gif" width="79"/></p>
<span class="tit"> </span>
<span class="date"> </span>
<span class="date"> </span>
</div>
<div class="select_infor">
<h3><img alt="선택내역" src="http://tkfile.yes24.com/img/perfsale/h3_tit_result01.gif"/></h3>
<ul>
<li><em><img alt="날짜" src="http://tkfile.yes24.com/img/perfsale/r_tit01.gif"/></em><span id="tk_day"> </span></li>
<li><em><img alt="시간" src="http://tkfile.yes24.com/img/perfsale/r_tit02.gif"/></em><span id="tk_time"> </span></li>
<li><em><img alt="매수" src="http://tkfile.yes24.com/img/perfsale/r_tit03.gif"/></em><span id="tk_count"> </span></li>
<li><em><img alt="좌석" src="http://tkfile.yes24.com/img/perfsale/r_tit04.gif"/></em>
<div id="tk_seat">
</div>
</li>
</ul>
</div>
<div class="pay_infor">
<h3><img alt="결제내역" src="http://tkfile.yes24.com/img/perfsale/h3_tit_result02.gif"/></h3>
<div class="link01">
<ul>
<li class="tk_price"><em><img alt="티켓금액" src="http://tkfile.yes24.com/img/perfsale/r_tit05.gif"/></em><span> </span></li>
<li class="tk_charge"><em><img alt="예매수수료" src="http://tkfile.yes24.com/img/perfsale/r_tit06.gif"/></em><span> </span></li>
<li class="tk_deli"><em><img alt="배송료" src="http://tkfile.yes24.com/img/perfsale/r_tit07.gif"/></em><span> </span></li>
<li class="tk_sumplus"><em><img alt="총금액" src="http://tkfile.yes24.com/img/perfsale/r_tit08.gif"/></em><span> </span></li>
</ul>
</div>
<div class="link02">
<ul>
<li class="tk_disc"><em><img alt="할인금액" src="http://tkfile.yes24.com/img/perfsale/r_tit09.gif"/></em><span> </span></li>
<li class="tk_coupon"><em><img alt="할인쿠폰" src="http://tkfile.yes24.com/img/perfsale/r_tit10.gif"/></em><span> </span></li>
<li class="tk_yesmoney"><em><img alt="YES머니" src="http://tkfile.yes24.com/img/perfsale/r_tit12.gif"/></em><span> </span></li>
<li class="tk_yesdeposit"><em><img alt="예치금" src="http://tkfile.yes24.com/img/perfsale/r_tit14.gif"/></em><span> </span></li>
<li class="tk_yesgift"><em><img alt="YES상품권" src="http://tkfile.yes24.com/img/perfsale/r_tit11.gif"/></em><span> </span></li>
<li class="tk_giftticket"><em><img alt="공연예매권" src="http://tkfile.yes24.com/img/perfsale/r_tit16.gif"/></em><span> </span></li>
<li class="tk_otherpays"><em><img alt="기타결제" src="http://tkfile.yes24.com/img/perfsale/r_tit17.gif"/></em><span> </span></li>
<li class="tk_summinus"><em><img alt="총할인금액" src="http://tkfile.yes24.com/img/perfsale/r_tit15.gif"/></em><span> </span></li>
</ul>
</div>
</div>
<span class="t_result"> <span>원</span></span>
<div class="btn">
<div class="tc" id="StepCtrlBtnPanel">
<div id="StepCtrlBtn01" style="display:none;">
<a class="dcursor" onclick="fdc_VerifySelSeatNumber();"><img alt="다음단계" src="http://tkfile.yes24.com/img/perfsale/btn_next04.gif"/></a>
</div>
<div id="StepCtrlBtn03" style="display:none;">
<a class="dcursor" onclick="fdc_GoPrevStep(jcSTEP1);"><img alt="이전단계" src="http://tkfile.yes24.com/img/perfsale/btn_prev.gif"/></a>
<a class="dcursor" onclick="fdc_PromotionEnd();"><img alt="다음단계" src="http://tkfile.yes24.com/img/perfsale/btn_next02.gif"/></a>
</div>
<div id="StepCtrlBtn04" style="display:none;">
<a class="dcursor" onclick="fdc_GoPrevStep(jcSTEP3);"><img alt="이전단계" src="http://tkfile.yes24.com/img/perfsale/btn_prev.gif"/></a>
<a class="dcursor" onclick="fdc_DeliveryEnd();"><img alt="다음단계" src="http://tkfile.yes24.com/img/perfsale/btn_next02.gif"/></a>
</div>
<div id="StepCtrlBtn05" style="display:none;">
<a class="dcursor" onclick="fdc_GoPrevStep(jcSTEP4);"><img alt="이전단계" src="http://tkfile.yes24.com/img/perfsale/btn_prev.gif"/></a>
<a class="dcursor" onclick="fdc_PrePayCheck();"><img alt="결제하기" id="imgPayEnd" src="http://tkfile.yes24.com/img/perfsale/btn_succ.gif"/></a>
</div>
</div>
</div>
</div>
</div>
<!--// 상황판 -->
</div>
<!-- 제 2 단계 : 좌석선택 (좌석플래시) -->
<div id="SeatFlashArea" style="display: none;">
<div class="seat_arrange">
<div class="f_header">
<ul>
<li>
<em><img alt="관람일변경" src="http://tkfile.yes24.com/img/perfsale/h3_tit_seat01.gif"/></em>
<span>
<select id="selFlashDateAll" onchange="fdc_selFlashDateAllChange(this.value);" style="width: 200px;"></select>
</span>
</li>
<li>
<em><img alt="회차변경" src="http://tkfile.yes24.com/img/perfsale/h3_tit_seat02.gif"/></em>
<span>
<select id="selFlashTime" onchange="fdc_SelFlashTimeChange(this.value);" style="width: 200px;"></select>
</span>
</li>
</ul>
</div>
<div id="divFlash"></div>
</div>
</div>
<!-- //제 2 단계 : 좌석선택 (좌석플래시) -->
<!-- 결과페이지 -->
<div id="SuccessBoard" style="display: none;">
<div class="success">
<div class="suc_tit">
<h2><img alt="결제가 정상적으로 완료되었습니다." src="http://tkfile.yes24.com/img/perfsale/h2_suc.gif"/></h2>
<p><img alt="예매 상세내역은 마이페이지 &gt; MY공연 &gt; 예매확인/취소에서 확인하실 수 있습니다." src="http://tkfile.yes24.com/img/perfsale/suc_txt.gif"/></p>
</div>
<div class="no_banner" id="BannerCtrl">
<div class="succ" id="SuccBook">
<h4><img alt="예매정보" src="http://tkfile.yes24.com/img/perfsale/suc_tit01.gif"/><img alt="예매완료" class="im_m3" id="bk_bookstatus" src="http://tkfile.yes24.com/img/perfsale/btn_suc.gif"/></h4>
<ul>
<li><em>예약번호</em><span class="red"><strong class="big" id="bk_bookno"> </strong><strong id="bk_tkcount"> </strong></span> </li>
<li><em>공연명</em><span><strong id="bk_perfname"> </strong></span></li>
<li><em>공연장</em><span><strong id="bk_theatername"> </strong></span></li>
<li><em>관람일시</em><span id="bk_viewtime"> </span></li>
<li>
<em>좌석<p><a href="javascript:;void(0);" id="bk_seatBtn" style="display:none"><img alt="좌석위치보기" src="http://tkfile.yes24.com/img/mypage/btn_chkseat.gif" style="margin-left:-7px"/></a></p> </em>
<div id="bk_tkseat"> </div>
</li>
<li>
<em>수령방법</em>
<span id="bk_deliveryinfo"> </span>
</li>
</ul>
<h4><img alt="유의사항" src="http://tkfile.yes24.com/img/perfsale/suc_tit02.gif"/></h4>
<ul>
<li>
<em>취소가능일시 :</em>
<span class="blu"><strong id="bk_canceltimeinfo"> </strong></span>
</li>
</ul>
</div>
<div class="succ" id="SuccPay">
<h4><img alt="결제정보" src="http://tkfile.yes24.com/img/perfsale/suc_tit03.gif"/></h4>
<ul class="pay">
<li><em>티켓금액</em><span id="sp_tkprice"> </span></li>
<li><em>예매수수료</em><span id="sp_charge"> </span></li>
<li><em>배송료</em><span id="sp_deli"> </span></li>
<li class="gry"><em><strong>(+)금액</strong></em><span><strong id="sp_sumplus"> </strong></span></li>
<li><em>할인금액</em><span id="sp_disc"> </span></li>
<li><em>할인쿠폰</em><span id="sp_coupon"> </span></li>
<li><em>YES머니</em><span id="sp_yesmoney"> </span></li>
<li><em>예치금</em><span id="sp_yesdeposit"> </span></li>
<li><em>YES24상품권</em><span id="sp_yesgift"> </span></li>
<li><em>공연예매권</em><span id="sp_giftticket"> </span></li>
<li><em>기타결제</em><span id="sp_otherpays"> </span></li>
<li class="gry"><em><strong>(-)금액</strong></em><span><strong id="sp_sumninus"> </strong></span></li>
<li class="total"><em>총 결제금액</em><span><strong id="sp_result"> </strong> 원</span></li>
<li class="total_p" style="display:none;"><em>YES포인트 예상 적립 금액</em><span><strong> </strong>원</span></li>
<li><em>결제수단</em><span id="sp_payinfo"> </span></li>
<li id="bank_accbank" style="display:none;"><em>입금계좌/은행</em><span id="sp_bank_accbank"> </span></li>
<li id="bank_amttime" style="display:none;"><em>입금금액/마감</em><span id="sp_bank_amttime"> </span></li>
</ul>
</div>
</div>
<div class="banner" style="display:none;">
<iframe allowtransparency="true" frameborder="0" id="ifrTicketBanner" scrolling="no" src="" style="display:block;"></iframe>
</div>
<div class="confirm">
<div class="tc">
<a class="dcursor" id="imgGoTicketView"><img alt="예매내역확인" src="http://tkfile.yes24.com/img/perfsale/btn_ok02.gif"/></a>
</div>
</div>
</div>
</div>
<!--// 결과페이지 -->
<!-- InicisPay 결제 및 주문을 위한 (지불/티켓) 전송 정보 DIV -->
<div class="PayInfoSendForm" id="divPayInfoSendForm"></div>
</div>
<!-- UI 영역 END -->
<img alt="ajaxLoader" id="imgAjaxLoader1_1" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader1_2" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader1_3" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader2_1" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader2_2" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader2_3" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader2_4" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader3_1" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader3_2" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader4_1" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader4_2" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader5_1" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader5_2" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader5_3" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader5_4" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader5_5" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader5_6" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader5_7" src="https://stkfile.yes24.com/img/ajax/loaderY.gif" style="display:none;"/><img alt="ajaxLoader" id="imgAjaxLoader6" src="https://stkfile.yes24.com/img/ajax/loader.gif" style="display:none;"/>
<!--이니시스 표준결제 필요기본정보-->
<div id="divInicisPayinfo" style="display:none"></div>
<!-- 전체영역에서 사용되는 중요보관 콘트롤 -->
<input id="IdTime" type="hidden"/>
<input id="IdSeatClassPrice" type="hidden"/>
<input id="IdSeatClass" type="hidden"/>
<input id="IdSeat" type="hidden"/>
<!-- 기타 DIV -->
<div id="divTimeTempData" style="display:none"></div>
<!-- 할인체크 DIV -->
<div id="SelPromotionStorage"></div>
<!-- 사용자 주소정보 보관 템플릿 DIV -->
<div id="divDeliveryUserInfo" style="display:none"></div>
<!-- 예매수수료 DIV -->
<div bkinloading="" id="divBookingFee" style="display:none"></div>
<!-- 기타 결제수단들(YES) 수신 정보 DIV -->
<div id="baseYesPays" style="display:none">
<div id="baseYesMoney"></div>
<div id="baseYesPoint"></div>
<div id="baseYesDeposit"></div>
<div id="baseYesGift"></div>
</div>
<!-- 예매권 사용 정보 DIV -->
<div id="divGiftTicketUsedInfo" style="display:none"></div>
<!-- 입금은행 OPTION 콘트롤 -->
<input id="hiddenBankOptions" type="hidden" value="&lt;option value='-1'&gt;입금은행 선택&lt;/option&gt;&lt;option value='50'&gt;국민은행&lt;/option&gt;&lt;option value='11631'&gt;기업은행&lt;/option&gt;&lt;option value='57'&gt;농협중앙회&lt;/option&gt;&lt;option value='11629'&gt;신한은행&lt;/option&gt;&lt;option value='49'&gt;우리은행&lt;/option&gt;&lt;option value='11634'&gt;우체국&lt;/option&gt;&lt;option value='11630'&gt;하나은행&lt;/option&gt;&lt;option value='11633'&gt;SC은행&lt;/option&gt;"/>
<!-- 현금영수증 발행 신청 정보 -->
<input id="hiddenReceiptInfo" receipt="" receiptno="" type="hidden"/>
<!-- 메시지 큐 -->
<div id="divMsgQueue" style="display:none"></div>
<!-- 가상계좌정보 DIV -->
<div id="divVBankInfo" style="display:none"></div>
<!-- 예스 포인트 -->
<div id="divYespointInfo" style="display:none"></div>
<!-- 결제 진행(바) 표시 DIV -->
<div id="divPayProgress" style="display:none;">
<table border="0" cellpadding="0" cellspacing="0" style="width:576px; height:265px;">
<tr>
<td align="center" style="background:url('http://tkfile.yes24.com/images/ticket/loading_box.gif') 0 0 no-repeat; padding-top: 10">
<table border="0" cellpadding="0" cellspacing="0">
<tr>
<td align="center" height="40" valign="top">
                                    결제 진행중입니다. 잠시만 기다려 주십시요.
                                </td>
</tr>
<tr>
<td>
<img alt="" src="http://tkfile.yes24.com/images/ticket/loading.gif"/>
</td>
</tr>
</table>
</td>
</tr>
</table>
</div>
<script type="text/javascript">
        //document.domain = "yes24.com";
        jgBookAlert = jgBookTAlert;
        jgBookPopup = jgBookTPopup;

        // Page 초기화 스크립트
        $j(document).ready(function () {

            if (window.opener == null) {
                alert("예매버튼을 이용하여 예매 부탁 드립니다.");
                location.href = "/pages/Main.aspx";
            }



            /*
            $j('body').siteSecurity({
                f12:'y'          //f12키 막기 사용여부
                ,rightclick: 'y' //우클릭 막기 사용여부
                ,select:'y'      //선택 막기 사용여부
                ,drag:'y'        //드래그 막기 사용여부
                //,execptionip:'1.1.1.1' //예외 아이피 사용여부
            });
            */




            if (jgIsPageShow) {
                // 전역변수 값설정 (서버연동이 필요한 경우만)
                jgOrdHeader = 'Y';
                jgIdPerf = '32098';
                jgIdSelTime = '';

                jgSeatSelectMax = parseInt('10');

                if (jgSeatSelectMax > 10) {
                    jgSeatSelectMax = 10;
                }

                var now = new Date();
                var txtDate = now.getFullYear() + jsf_def_PadLeft(now.getMonth() + 1, 2) + jsf_def_PadLeft(now.getDate(), 2) + jsf_def_PadLeft(now.getHours(), 2) + jsf_def_PadLeft(now.getMinutes(), 2);

                if (jgIdPerf == "17519" || jgIdPerf == "17527") {

                    $j("#cbxYesMoney").attr("onclick", "").unbind('click');
                    $j("#imgExchangePoint").attr("onclick", "").unbind('click');
                    $j("#cbxYesDeposit").attr("onclick", "").unbind('click');
                    $j("#imgYesGiftUse").attr("onclick", "").unbind('click');
                    $j("#imgGiftTicketRegUse").attr("onclick", "").unbind('click');
                    //                    if (parseInt(txtDate) < parseInt("201404091200")) {
                    $j("#liBenepiaPoint").attr("onclick", "").unbind('click');
                    //}

                    $j("#txtYesMoney").attr("onchange", "").unbind('change');
                    $j("#txtYesDeposit").attr("onchange", "").unbind('change');
                    $j("#txtYesGift").attr("onchange", "").unbind('change');

                    $j("#imgExchangePoint").css("cursor", "");
                    $j("#imgYesGiftUse").css("cursor", "");
                    $j("#imgGiftTicketRegUse").css("cursor", "");
                    $j("#liYesMoney").css("display", "none");
                    $j("#liYesPoint").css("display", "none");
                    $j("#liYesDeposit").css("display", "none");
                    $j("#liYesGift").css("display", "none");
                    $j("#liGiftTicket").css("display", "none");
                    $j("#liBenepiaPoint").css("display", "none");
                    $j("#step05").find(".mb").find(".d_line").css("display", "none");
                }

//                if (jgIdPerf == "25520" || jgIdPerf == "25609") {

//                    if (parseInt(txtDate) < parseInt("201611241200")) {
//                        $j("#cbxYesMoney").attr("onclick", "").unbind('click');
//                        $j("#imgExchangePoint").attr("onclick", "").unbind('click');
//                        $j("#cbxYesDeposit").attr("onclick", "").unbind('click');
//                        $j("#imgYesGiftUse").attr("onclick", "").unbind('click');
//                        $j("#imgGiftTicketRegUse").attr("onclick", "").unbind('click');
//                        $j("#liBenepiaPoint").attr("onclick", "").unbind('click');
//                        $j("#txtYesMoney").attr("onchange", "").unbind('change');
//                        $j("#txtYesDeposit").attr("onchange", "").unbind('change');
//                        $j("#txtYesGift").attr("onchange", "").unbind('change');

//                        $j("#imgExchangePoint").css("cursor", "");
//                        $j("#imgYesGiftUse").css("cursor", "");
//                        $j("#imgGiftTicketRegUse").css("cursor", "");
//                        $j("#liYesMoney").hide();
//                        $j("#liYesPoint").hide();
//                        $j("#liYesDeposit").hide();
//                        $j("#liYesGift").hide();
//                        $j("#liGiftTicket").hide();
//                        $j("#liBenepiaPoint").hide();

//                    }
//                }



                jgSaleChannel = '1';
                jgIsMPoint = '0';
                jgIsHcardOpt = '0';

                jgIsShowOKCashbag = parseInt('0');
                jgIsShowBenepia = parseInt('0');

                jgValleyCount = parseInt('-2');
                jgCampingCount = parseInt('-1');
                jgJisanTotalCount = parseInt('-1');

                jgCampConcertCnt = parseInt('-1'); //캠핑권(2일권)
                jgCampConcertCnt2 = parseInt('-1'); //캠핑권(2일권)
                jgclassCount_1 = parseInt('-1'); //캠핑권(금토)
                jgclassCount_2 = parseInt('-1'); //3일권
                jgclassCount_3 = parseInt('-1'); //캠핑권(토일)


                jgPerfOption = '0';
                jgSaleLimitNo = '0';
                jgPerfFanClubJoin = '0';
                jgPerfHappyFamily = '0';

                jgRushTime = parseInt('0');
                jgUseReward = 'True';
                jgIsInterparkProduct = ('' == '342');
                jgAdultAuthDetailUse = '0';
                jgAdultAuthSaleUse = '0';
                jgYesPointState = '0';

                jgJenreName = '콘서트';
                jgSubGenre = 15463  ;

                jgIsMania = '0';

                reCAPTCHAUse = 'Y';

                if (reCAPTCHAUse == "1") {
                    Recaptcha.create("6LcSdBsTAAAAADLyhX6zOcjum6jaxA9nF2-u2CSA",
                    "recaptcha_div", {
                        theme: "custom",
                        callback: Recaptcha.focus_response_field
                    });
                }

                $j("#progressBar").jry_home_ShowProgressBar({ "state": "stop" });

                if ('1' != '0') {// 로그인 한 경우
                    if (jgSeatSelectMax == 0) {// 예매 가능 매수가 없을 경우
                        $j("#ContentsArea").css("display", "none");

                        if (jgBookAlert == jcMODE_JQUERY) {// JQuery MODE
                            $j("#dialogAlert").jAlert({
                                "msg": '예매 가능한 매수가 초과 되었습니다.<br />본 공연은 최대 <font color=red>10 매</font>까지만<br />예매가 가능합니다.',
                                'buttons': { '확인': function () { $j(this).dialog('close'); fts_Close(false); } }
                            });
                        } else {// Window MODE
                            alert('예매 가능한 매수가 초과 되었습니다.<br />본 공연은 최대 <font color=red>10 매</font>까지만<br />예매가 가능합니다.');
                            fts_Close(false);
                        }
                    }
                    else {// 예매 가능 매수가 있을 경우
                        fdc_CtrlStep(jcSTEP1);
                    }
                }
                else {// 로그인을 안 한 경우
                    // 예매진행 영역 숨김
                    $j("#ContentsArea").css("display", "none");
                }

                if (jgBannerMode == jcBANNER_ON) {
                    $j("#ifrTicketBanner").attr("src", '/Pages/Perf/Sale/Banner/PerfSaleBanner.aspx');
                }

                $j("#step04_DeliveryInfo").find("#deliveryZipCode1, #deliveryZipCode2").unbind('.Addr_NoInput').bind('keydown.Addr_NoInput', jsf_def_NoInput).bind('paste.Addr_NoInput', jsf_def_NoPaste).bind('cut.Addr_NoInput', jsf_def_NoCut);
                $j("#step04_DeliveryInfo input[id^='deliveryMobile']:text, #step04_OrdererInfo input[id^='ordererMobile']:text").
                    unbind('.delivery_onlynumber').bind('blur.delivery_onlynumber_onlynumber', jsf_def_InputBlur).bind('keydown.delivery_onlynumber_onlynumber', jsf_def_InputOnlyNumber);

                $j("#step04_OverseasDeliveryInfo input[id^='overseasDeliveryMobile']:text").
                    unbind('.delivery_onlynumber').bind('keydown.overseasDelivery_onlynumber_onlynumber', jsf_def_InputOnlyNumberOkDash);
                $j("#step04_OverseasDeliveryInfo input[id^='overseasDeliveryZipcode']:text").
                    unbind('.delivery_onlynumber').bind('keydown.overseasDelivery_onlynumber_onlynumber', jsf_def_InputOnlyNumberOkCharacter);

                $j("#txtLiveRefundAccount").unbind('.delivery_onlynumber').bind('keydown.overseasDelivery_onlynumber_onlynumber', jsf_def_InputOnlyNumberOkDash);

                jsf_com_IE9NoSelect($j("#txtYesMoney, #txtYesDeposit, #txtYesGift"));
            }




        });


        (function($j){
	        var opt,ele;

	        $j.fn.siteSecurity = function(option){
		        ele = $j(this);
		        opt = option;

                /*
		        if(opt.exceptionip!=''){
			        $j.get("http://ipinfo.io", function(res) {
				        resconverter(res.ip);
			        }, "jsonp");
		        }else{
			        resconverter(false);
		        }
                */

                resconverter(false);


		        function resconverter(ip){
			        //if(opt.exceptionip!=ip || ip===false){
                    if(ip===false){

				        if(opt.f12=='y'){
					        ele.bind('keydown',function(e){
						        if(e.keyCode==123){
							        e.preventDefault();
						        }
					        });
				        }

				        if(opt.rightclick=='y'){
					        $j(document).bind("contextmenu", function(){return false;});
				        }

				        if(opt.select=='y'){
					        $j(document).bind('selectstart',function() {return false;});
				        }

				        if(opt.drag=='y'){
					        $j(document).bind('dragstart',function(){return false;});
				        }
			        }
		        }


	        }
        })(jQuery);

    </script>
<!-- WEMS TRACKING SCRIPT CODE START -->
<!-- DO NOT MODIFY THIS SCRIPT CODE. -->
<!-- COPYRIGHT (C) 1999-2008 NETHRU INC. ALL RIGHTS RESERVED. -->
<script src="http://www.yes24.com/javascript/wlo.js" type="text/javascript"></script>
<script type="text/javascript">
//    (function () {
//        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
//        ga.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'www.yes24.com/javascript/wlo.js';
//        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
//    })();

    _n_sid = "08070200045";
    _n_uid_cookie = "Mallinmall_CKMI";
    _n_info1_cookie = "PID";
    n_logging();
</script>
<!-- WEMS TRACKING SCRIPT CODE END -->
<script type="text/javascript">
<!--
    var _ekamsAdvertiserID= 546;
//-->
</script>
<script src="/inc/js/yes24/roiJsNewScript_v3.js" type="text/javascript"></script>
<script src="/inc/comas/comas.js" type="text/javascript"></script>
<!-- Google Code for &#44396;&#47588;/&#54032;&#47588; Conversion Page -->
<script type="text/javascript">

    var google_conversion_id = 1056776890;
    var google_conversion_language = "en";
    var google_conversion_format = "1";
    var google_conversion_color = "666666";
    var google_conversion_label = "OszoCMasPhC6xfT3Aw";
    var google_conversion_value = 0;
    var google_remarketing_only = false;

</script>
<script src="http://www.googleadservices.com/pagead/conversion.js" type="text/javascript"></script>
<noscript>
<div style="display:inline;">
<img alt="" height="1" src="http://www.googleadservices.com/pagead/conversion/1056776890/?value=0&amp;label=OszoCMasPhC6xfT3Aw&amp;guid=ON&amp;script=0" style="border-style:none;" width="1"/>
</div>
</noscript>
</body>
</html>