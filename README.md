# FLIX Project Front-end/Back-end 소개

### OTT 서비스 제공 사이트 NETFLIX 클론 프로젝트

## 📍 프로젝트 소개
OTT(Over The Top) 서비스 제공 사이트 NETFLIX를 클론 코딩하였습니다.
agile 방법론을 활용한 scrum 방식으로 프로젝트를 진행했습니다. 
MAU를 고려해 기존 페이스북만 제공되던 소셜로그인을 카카오, 구글로 변경하는 등 기존 사이트에서 인식한 문제점을 코드로 개선하려고 노력하였습니다. 

## 📍 개발 인원 및 기간
개발기간 : 2021.09.13 - 2021.10.01
개발 인원 : 프론트엔드 3명, 백엔드 2명
개발자

- FE: 김동희 김승찬 박은정
- BE: 고준영 김장호

## 📍 기술스택

- Javascript (ES6+)
- React with Hooks, React Router
- styled-components
- Python3
- Django

### 협업도구

- Slack
- Git & Github
- Trello
- POSTMAN


## 📍 시연 영상
<a href="">시연 영상 보러가기</a>

##### Reference

- 이 프로젝트는 [NETFLIX](https://www.netflix.com/browse) 사이트를 참조하여 학습목적으로 만들었습니다
- 학습수준의 프로젝트로 만들었기 때문에 이 코드 및 데모영상을 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될  수 있습니다
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.

<br>

## 📍 Teammate

<div id=teammate>
  <h4> Front-End </h4>
  <table style="text-align:center;">
    <tr>
      <th><a href="https://github.com/dev-bomdong">김동희</a></th>
      <th><a href="https://github.com/tmdckszm">김승찬</a></th>
      <th><a href="https://github.com/eunjeong-97">박은정</a></th>
    </tr>
    <tr>
      <td>
        - 데이터 값에 따라 이동거리가 달라지는 Carousel Slide 구현<br>
        - Portal을 통한 Modal 구현<br>
        - 페이지, Carousel, Modal component 간 라우팅 연결
      </td>
      <td>
        - scroll에 따라 스타일링이 변화하는 nav bar, footer 구현<br>
        - 메인페이지 및 modal창 내 비디오 스트리밍 구현<br>
        - 페이지, Carousel, Modal component 간 라우팅 연결
      </td>
      <td>
        - 유효성 검사를 포함한 회원가입 기능 구현<br>
        - 유효성 검사 및 token을 부여하는 로그인 기능 구현<br>
        - kakao, google 소셜 로그인 기능 구현<br>
        - modal 내의 하트 아이콘 클릭을 통한 '찜하기' 기능 및 찜하기 리스트 기능 구현
      </td>
    </tr>
  </table>
  <br>
  <h4> Back-End </h4>
  <table style="text-align:center;">
    <tr>
      <th><a href="https://github.com/jay95ko">고준영</a></th>
      <th><a href="https://github.com/flow2lime">김장호</a></th>
    </tr>
    <tr>
      <td>
        - StreamingHttpResponse 와 S3를 이용한 스트리밍 서비스<br>
        - jwt토큰과 이를통한 얻어진 권한을 활용한 찜하기 기능 구현<br>
        - Docker, EC2, RDS, S3를 활용한 배포
      </td>
      <td>
        - Flix 서비스 회원가입, 로그인 API 구현<br>
        - 카카오, 구글 로그인 API 구현
      </td>
    </tr>       
  </table>
  <br>
</div>
