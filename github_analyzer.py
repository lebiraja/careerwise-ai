from github import Github
from typing import Dict, List, Set
import os
from github.GithubException import RateLimitExceededException, BadCredentialsException

def analyze_github(username: str) -> Dict[str, any]:
    """
    Analyze a user's public GitHub profile and repositories.
    Returns a dictionary with repo count, languages, stars, and activity.
    """
    try:
        # Initialize GitHub client
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            return {"error": "No GITHUB_TOKEN found in .env. Please set a valid token."}
        
        g = Github(github_token)
        user = g.get_user(username)

        # Initialize output dictionary
        github_data = {
            "repo_count": 0,
            "languages": [],
            "total_stars": 0,
            "commit_frequency": 0,
            "readme_quality": "Basic"
        }

        # Get public repositories
        repos = user.get_repos()
        github_data["repo_count"] = repos.totalCount

        # Analyze languages and stars
        languages: Set[str] = set()
        total_stars = 0
        total_commits = 0
        has_readme = 0
        for repo in repos:
            repo_langs = repo.get_languages()
            languages.update(lang.lower() for lang in repo_langs.keys())
            total_stars += repo.stargazers_count
            total_commits += repo.get_commits().totalCount
            try:
                repo.get_readme()
                has_readme += 1
            except:
                pass

        github_data["languages"] = list(languages)
        github_data["total_stars"] = total_stars
        github_data["commit_frequency"] = total_commits / max(1, github_data["repo_count"])
        github_data["readme_quality"] = (
            "Good" if has_readme / max(1, github_data["repo_count"]) > 0.5 else "Basic"
        )

        return github_data

    except RateLimitExceededException:
        return {"error": "GitHub API rate limit exceeded. Check GITHUB_TOKEN in .env or wait and try again."}
    except BadCredentialsException:
        return {"error": "Invalid GITHUB_TOKEN. Please update .env with a valid token."}
    except Exception as e:
        return {"error": f"Failed to analyze GitHub: {str(e)}"}