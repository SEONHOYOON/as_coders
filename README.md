# 학습조직 시작하기 전 읽어주세요

0. (windows 의 경우) git 다운로드
~~~
$ git init
$ git status
~~~
1. 원격저장소 연결

    1. 최초 작업시 - clone
    ~~~
    $ git clone https://github.com/coders-as/as_coders
    $ git remote -v 실행시 원격저장소명 origin 확인
    ~~~
    2. 기존 연결된 저장소가 있을 때 - pull
    ~~~
    $ git pull
    ~~~

2. branch 생성
~~~
$ git branch [branch_name]
$ git checkout [branch name]
~~~

3. local PC 에서 작업 후 add, commit, push 진행
~~~
$ git add [file_path] / git add * / git add . (해당 폴더 내에서)
$ git commit $m "[comment]"
$ git push origin [branch_name]
~~~
* 참조
![](https://www.secmem.org/assets/images/git_pr/git_transaction.png)

4. pull request 생성
- 본인 github 저장소에서 Compare & pull reqeust 버튼 클릭
- 메시지를 작성하고 PR을 생성

5. PR을 받은 관리자는 메시지란에 코드 리뷰 작성 이후 Merge
