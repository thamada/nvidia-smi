import requests
import mdv

def display_markdown_with_mdv_from_github(url):
    try:
        # GitHubのURLからMarkdownファイルを取得
        response = requests.get(url)
        response.raise_for_status()
        md_text = response.text

        # mdvを使ってMarkdownを装飾して表示
        rendered = mdv.main(md_text)
        print(rendered)

    except requests.exceptions.RequestException as e:
        print(f"エラーが発生しました: {e}")

def main():
    # GitHub上のREADME.mdファイルのURLを指定
    #github_url = "https://github.com/thamada/nvidia-smi/blob/main/README.md"
    github_url = "https://github.com/thamada/nvidia-smi/raw/refs/heads/main/README.md"


    # GitHubのREADME.mdを装飾して表示
    display_markdown_with_mdv_from_github(github_url)

