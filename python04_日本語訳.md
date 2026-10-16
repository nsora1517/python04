# Data Archivist — サイバーアーカイブにおけるデジタル保存

> **概要:** ファイル操作をマスターし、データストリームを管理し、情報を守る堅牢なアーカイブシステムを構築することで、デジタルの知識を保存しよう。
>
> **バージョン:** 3.0

---

## 目次

- [第I章 はじめに](#第i章-はじめに)
- [第II章 AI利用に関する指示](#第ii章-ai利用に関する指示)
- [第III章 共通ルール](#第iii章-共通ルール)
  - [III.1 一般ルール](#iii1-一般ルール)
  - [III.2 出力仕様](#iii2-出力仕様)
- [第IV章 演習0: Ancient Text Recovery](#第iv章-演習0-ancient-text-recovery)
- [第V章 演習1: Archive Creation](#第v章-演習1-archive-creation)
- [第VI章 演習2: Stream Management](#第vi章-演習2-stream-management)
- [第VII章 演習3: Vault Security](#第vii章-演習3-vault-security)
- [第VIII章 提出方法](#第viii章-提出方法)

---

## 第I章 はじめに

**サイバーアーカイブへようこそ！**

2087年、人類にとって最大の宝は金でもダイヤモンドでもなく、**データ**です。古代のミームから量子アルゴリズムまで、あらゆるデジタル知識は広大なサイバーアーカイブに保管されています。しかしデータは壊れやすいものです。適切に保存しなければ、デジタルの虚空へと永遠に消えてしまいます。

そこであなたの出番です。データアーキビストとして、あなたの使命は古より伝わる**ファイル操作**の技術をマスターし、どんな知識も決して失われないようにすることです。

あなたの道具はシンプルですが強力です。データ保管庫を**開く(open)**、その中身を**読む(read)**、新しいアーカイブを**書く(write)**、そして最も重要なのが、貴重な情報を失うことなく**予期せぬ事態に対処する**能力です。

アーカイブはあなたを頼りにしています！

---

## 第II章 AI利用に関する指示

### ● 背景

学習の過程で、AIはさまざまなタスクを手助けしてくれます。AIツールのさまざまな能力と、それらがどのようにあなたの作業を支援できるかを探求する時間を取りましょう。ただし、常に慎重に向き合い、結果を批判的に評価してください。コード、ドキュメント、アイデア、技術的な説明のいずれであっても、自分の質問が適切だったか、生成された内容が正確かどうかを完全に確信することはできません。仲間(peers)は、ミスや盲点を避けるための貴重なリソースです。

### ● 主なメッセージ

- 繰り返しの作業や面倒な作業を減らすためにAIを使いましょう。
- 将来のキャリアに役立つプロンプト作成スキル(コーディング・非コーディングの両方)を身につけましょう。
- AIシステムの仕組みを学び、よくあるリスク、バイアス、倫理的問題を予測・回避できるようにしましょう。
- 仲間と協力しながら、技術的スキルとパワースキル(対人スキル)の両方を伸ばし続けましょう。
- **自分が完全に理解し、責任を持てるAI生成コンテンツだけを使いましょう。**

### ● 学習者のルール

- AIツールを探求し、その仕組みを理解する時間を取りましょう。そうすることで、倫理的に使い、潜在的なバイアスを減らすことができます。
- プロンプトを書く前に問題についてよく考えましょう。そうすることで、正確な用語を使った、より明確で詳細かつ的確なプロンプトを書けるようになります。
- AIが生成したものは、体系的に確認・レビュー・疑問視・テストする習慣を身につけましょう。
- 常に仲間のレビューを求めましょう。自分だけの検証に頼ってはいけません。

### ● このフェーズで得られる成果

- 汎用的なプロンプトスキルと、分野特化型のプロンプトスキルの両方を身につける。
- AIツールを効果的に使い、生産性を高める。
- 計算論的思考、問題解決力、適応力、協調性を引き続き強化する。

### ● コメントと例

- 試験や評価など、本当の理解を示さなければならない場面に定期的に出会います。準備を怠らず、技術スキルと対人スキルの両方を伸ばし続けましょう。
- 自分の考えを説明したり仲間と議論したりすると、理解の穴が見つかることがよくあります。ピアラーニングを優先しましょう。
- AIツールはあなた固有の文脈を知らないことが多く、一般的な回答をしがちです。同じ環境を共有する仲間なら、より的確で正確な洞察を与えてくれます。
- AIは最もありそうな答えを生成する傾向がありますが、仲間は別の視点や貴重なニュアンスを提供してくれます。品質のチェックポイントとして仲間を頼りましょう。

#### ✅ 良い例

> AIに「ソート関数をテストするにはどうすればいい？」と聞く。いくつかアイデアをもらう。それらを試して、結果を仲間と一緒にレビューする。一緒にやり方を改善していく。

#### ❌ 悪い例

> AIに関数をまるごと書かせて、プロジェクトにコピペする。相互評価で、それが何をしているのか、なぜそうなのかを説明できない。信用を失い、プロジェクトに落ちる。

#### ✅ 良い例

> パーサーの設計をAIに手伝ってもらう。その後、仲間と一緒にロジックを一つずつ確認する。バグを2つ見つけ、一緒に書き直す。より良く、よりきれいで、完全に理解したコードになる。

#### ❌ 悪い例

> プロジェクトの重要な部分のコードをCopilotに生成させる。コンパイルは通るが、パイプをどう扱っているのか説明できない。評価中に説明できず、プロジェクトに落ちる。

---

## 第III章 共通ルール

### III.1 一般ルール

- すべてのプログラムは **Python 3.10 以降** で書くこと。
- コードは **flake8** リンターの基準に準拠すること。
- すべての関数とメソッドに**型ヒント**を付けること。**mypy** で確認すること。
- 関数は例外を適切に処理し、クラッシュしないようにすること。
- 作業は指定されたGitリポジトリに提出すること。
- 評価されるのはこのリポジトリ内の内容のみです。

> **上級者向けの注意:** `with` 文は**演習3で導入されます**。それより前の演習では使ってはいけません。

> 以下の標準の型とコレクションは、それらに関連するすべてのメソッドとコンストラクタを含めて使用が許可されています: `str`, `int`, `float`, `list`, `dict`, `set`, `tuple`

### III.2 出力仕様

各演習には、推奨される出力形式を示すターミナルの例が載っています。基本的な構造は守る必要がありますが、本質的な情報が保たれている限り、ファイル操作についての自分の理解を反映するようにメッセージをカスタマイズしても構いません。

---

## 第IV章 演習0: Ancient Text Recovery

| 項目 | 内容 |
|---|---|
| 演習 | 0 |
| 名前 | ft_ancient_text |
| ディレクトリ | `ex0/` |
| 提出ファイル | `ft_ancient_text.py` |
| 使用許可 | `import sys`, `sys.argv`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.close()`, `print()` |

**ミッション概要:** アーカイブは保管庫7で古代のデータ断片を発見しました。データアーキビストとしての最初の任務は、この貴重な情報がさらに劣化する前に復元することです。

コマンドラインからファイル名を受け取り、そのファイルの内容を読み込んで、**`cat` コマンドと同じように表示**してください。例のように、ヘッダーとフッターをいくつか追加します。さまざまな失敗ケース(存在しないファイル、アクセスできないファイルなど)を処理する必要があります。

> **考えてみよう:** `open()` が返すデータの型は何でしょう？

### 実行例

```
$> cat ancient_fragment.txt
[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion

$> python3 ft_ancient_text.py
Usage: ft_ancient_text.py <file>

$> python3 ft_ancient_text.py foo
=== Cyber Archives Recovery ===
Accessing file 'foo'
Error opening file 'foo': [Errno 2] No such file or directory: 'foo'

$> python3 ft_ancient_text.py /etc/master.passwd
=== Cyber Archives Recovery ===
Accessing file '/etc/master.passwd'
Error opening file '/etc/master.passwd': [Errno 13] Permission denied: '/etc/master.passwd'

$> python3 ft_ancient_text.py ancient_fragment.txt
=== Cyber Archives Recovery ===
Accessing file 'ancient_fragment.txt'
---

[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion

---
File 'ancient_fragment.txt' closed.
```

---

## 第V章 演習1: Archive Creation

| 項目 | 内容 |
|---|---|
| 演習 | 1 |
| 名前 | ft_archive_creation |
| ディレクトリ | `ex1/` |
| 提出ファイル | `ft_archive_creation.py` |
| 使用許可 | `import sys`, `sys.argv`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.write()`, `io.close()`, `print()`, `input()` |

**ミッション概要:** データ復元、見事でした！次の任務は、新しいアーカイブエントリを作成して、新たな保存プロトコルを確立することです。

前の演習で作ったコードを使ってください。スクリプトの最後に、以下のようにコードを改良します:

- 各行の末尾に特別なアーカイブ文字(`#` 文字)を追加する(2087年互換にするため、ということにしておきましょう)
- 新しい内容を表示する
- 保存先のファイル名をユーザーに尋ねる。何も保存しない場合は空のままにできる
- ファイル名が入力された場合は新しい内容を保存し、新しい終了メッセージを表示する

> ファイルを作成してください。すでに存在する場合は上書きします。

### 実行例

```
$> python3 ft_archive_creation.py ancient_fragment.txt
=== Cyber Archives Recovery & Preservation ===
Accessing file 'ancient_fragment.txt'
---

[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion

---
File 'ancient_fragment.txt' closed.

Transform data:
---

[FRAGMENT 001] Digital preservation protocols established 2087#
[FRAGMENT 002] Knowledge must survive the entropy wars#
[FRAGMENT 003] Every byte saved is a victory against oblivion#

---
Enter new file name (or empty):
Not saving data.

$> python3 ft_archive_creation.py ancient_fragment.txt
=== Cyber Archives Recovery & Preservation ===
Accessing file 'ancient_fragment.txt'
---

[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion

---
File 'ancient_fragment.txt' closed.

Transform data:
---

[FRAGMENT 001] Digital preservation protocols established 2087#
[FRAGMENT 002] Knowledge must survive the entropy wars#
[FRAGMENT 003] Every byte saved is a victory against oblivion#

---
Enter new file name (or empty): new_fragment.txt
Saving data to 'new_fragment.txt'
Data saved in file 'new_fragment.txt'.

$> cat new_fragment.txt
[FRAGMENT 001] Digital preservation protocols established 2087#
[FRAGMENT 002] Knowledge must survive the entropy wars#
[FRAGMENT 003] Every byte saved is a victory against oblivion#
```

---

## 第VI章 演習2: Stream Management

| 項目 | 内容 |
|---|---|
| 演習 | 2 |
| 名前 | ft_stream_management |
| ディレクトリ | `ex2/` |
| 提出ファイル | `ft_stream_management.py` |
| 使用許可 | `import sys`, `sys.argv`, `sys.stdin`, `sys.stdout`, `sys.stderr`, `len()`, `open()`, `import typing`, `typing.IO`, `io.read()`, `io.readline()`, `io.write()`, `io.flush()`, `io.close()`, `print()` |

**ミッション概要:** アーカイブは、デジタル文明の創設以来ずっと稼働している3つの神聖なデータチャネルを通じて動いています。インターネットそのものよりも古いこれらのチャネルをマスターしましょう！

前の演習で作ったコードを使ってください。以下のように更新します:

- 例外から生じたエラーメッセージを、標準出力ではなく**エラー出力ストリーム(標準エラー出力)**に、分かりやすいプレフィックスを付けて出力する(例を参照)
- **組み込み関数 `input()` を使わずに**ユーザー入力を受け取る

### 実行例

```
$> python3 ft_stream_management.py foo
=== Cyber Archives Recovery & Preservation ===
Accessing file 'foo'
[STDERR] Error opening file 'foo': [Errno 2] No such file or directory: 'foo'

$> python3 ft_stream_management.py ancient_fragment.txt
=== Cyber Archives Recovery & Preservation ===
Accessing file 'ancient_fragment.txt'
---

[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion

---
File 'ancient_fragment.txt' closed.

Transform data:
---

[FRAGMENT 001] Digital preservation protocols established 2087#
[FRAGMENT 002] Knowledge must survive the entropy wars#
[FRAGMENT 003] Every byte saved is a victory against oblivion#

---
Enter new file name (or empty): /etc/passwd
Saving data to '/etc/passwd'
[STDERR] Error opening file '/etc/passwd': [Errno 13] Permission denied: '/etc/passwd'
Data not saved.
```

---

## 第VII章 演習3: Vault Security

| 項目 | 内容 |
|---|---|
| 演習 | 3 |
| 名前 | ft_vault_security |
| ディレクトリ | `ex3/` |
| 提出ファイル | `ft_vault_security.py` |
| 使用許可 | `open()`, `read()`, `write()`, `print()` |

**ミッション概要:** 主任アーキビストがあなたの素質に目を留め、保管庫セキュリティ部門へ昇進させることにしました。ここは本物のアーキビストが実力を証明する場所です。

この演習では、ファイルを適切に扱うために **`with` 文(コンテキストマネージャ)** を使う必要があります。`with` 文は、エラーが起きた場合でもファイルを自動的に閉じてくれるので、リソースリークを防げます。

どんなファイルにも安全に読み書きできる関数 **`secure_archive()`** を作成してください。この関数は **タプル `(True|False, str)`** を返します。真偽値は処理が成功したかどうかを示し、文字列はそれに関連する内容(ファイルの中身、またはエラーメッセージ)です。

関数は次の引数を受け取ります:

1. **必須**のファイル名
2. 実行する処理(読み込みか書き込みか)を示す、**省略可能な** `int` または `str`(どちらにするかは自由)
3. ファイルに書き込む内容を含む、**省略可能な**もう1つの文字列

> ディフェンス(評価)では、コードの構造がこれらの要件に合っているかが確認されます。

### 実行例

```
$> python3 ft_vault_security.py
=== Cyber Archives Security ===

Using 'secure_archive' to read from a nonexistent file:
(False, "[Errno 2] No such file or directory: '/not/existing/file'")

Using 'secure_archive' to read from an inaccessible file:
(False, "[Errno 13] Permission denied: '/etc/master.passwd'")

Using 'secure_archive' to read from a regular file:
(True, '[FRAGMENT 001] Digital preservation protocols established 2087\n[FRAGMENT 002] Knowledge must survive the entropy wars\n[FRAGMENT 003] Every byte saved is a victory against oblivion\n')

Using 'secure_archive' to write previous content to a new file:
(True, 'Content successfully written to file')
```

---

## 第VIII章 提出方法

いつも通り、課題を自分の**Git**リポジトリに提出してください。ディフェンス(評価)ではリポジトリ内の作業だけが評価されます。ファイル名が正しいか、ためらわずに再確認しましょう。

> 評価中に、ファイル操作について説明したり、エラー処理を実演したり、`with` 文がどう動くかを見せたりするよう求められることがあります。各演習の背景にある概念を理解しておきましょう。

> 提出するのは、プロジェクトの仕様で求められているファイルだけです。ファイル操作への理解がはっきり伝わる、きれいでシンプルなコードを心がけましょう。
