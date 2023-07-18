import git

if __name__ == '__main__':
    repo = git.Repo(search_parent_directories=True)

    def commit_history():
        commit_his = dict()
        for branch in repo.branches:
            print(f'Branch: {branch.name}')
            commits = list(repo.iter_commits(branch))
            for commit in commits:
                print(f'  Commit: {commit.hexsha} - {commit.message.strip()}')
                commit_his[branch.name + '/' + commit.hexsha] = dict()
                commit_his[branch.name + '/' + commit.hexsha]['message'] = commit.message.strip()
                commit_his[branch.name + '/' + commit.hexsha]['parents'] = [parent.hexsha for parent in commit.parents]
                commit_his[branch.name + '/' + commit.hexsha]['author'] = commit.author.name
                commit_his[branch.name + '/' + commit.hexsha]['time'] = commit.authored_datetime
        return commit_his