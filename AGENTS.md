# AGENTS.md - math-friends (점박이 숫자 친구들)

초등 수학 무료 학습지 생성기. 공개 저장소이며 CC BY-NC-SA 4.0 + 상업 이용은 별도 계약(이중 라이선스).

## Git

| | |
|---|---|
| 원격 | `java-jaydev/math-friends` (public) |
| gh 계정 | `java-jaydev` |

원격 작업 전 `gh auth status` 로 활성 계정 확인. 다르면 `gh auth switch --user java-jaydev`.
커밋 작성자는 이 저장소 로컬 설정(`java-jaydev`, GitHub noreply 이메일)을 쓴다. 전역 git 설정을 쓰지 않는다.

## 규칙

- `private/` 는 개인 학습 기록이다. 절대 커밋하지 않는다(.gitignore 에 있음). 공개 문서에는 특정 아이 정보를 쓰지 않는다.
- 외부 Pull Request 는 받지 않는다. 이슈만 받는다.
- 캐릭터는 오리지널만 쓴다. 기존 캐릭터(포켓몬 등)를 그리거나 닮게 만들지 않는다.
- 캐릭터 그림은 Codex 이미지 생성으로 만들고, 새 그림은 `assets/numfriends_sheet.png` 와 `assets/turnaround/` 를 참고 이미지로 넣어 모습을 유지한다.
- 학습지 수정 후 `python3 worksheets/build.py <seed>` 로 PDF 를 만들고, 페이지를 이미지로 렌더링해 넘침·겹침을 눈으로 확인한다.
