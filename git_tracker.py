import git

if __name__ == '__main__':
    repo = git.Repo(search_parent_directories=True)

    def commit_history():
        commit_history = dict()
        for branch in repo.branches:
            print(f'Branch: {branch.name}')
            commits = list(repo.iter_commits(branch))
            for commit in commits:
                print(f'  Commit: {commit.hexsha} - {commit.message.strip()}')
                commit_history[branch.name + '/' + commit.hexsha] = dict()
                commit_history[branch.name + '/' + commit.hexsha]['message'] = commit.message.strip()
                commit_history[branch.name + '/' + commit.hexsha]['parents'] = [parent.hexsha for
                                                                                parent in commit.parents]
                commit_history[branch.name + '/' + commit.hexsha]['author'] = commit.author.name
                commit_history[branch.name + '/' + commit.hexsha]['time'] = commit.authored_datetime
        return commit_history


    def commit_history_simple():
        commit_history = dict()
        for branch in repo.branches:
            print(f'Branch: {branch.name}')
            commits = list(repo.iter_commits(branch))
            for commit in commits:
                print(f'  Commit: {commit.hexsha} - {commit.message.strip()}')
                if commit.hexsha not in commit_history.keys():
                    commit_history[commit.hexsha] = dict()
                commit_history[commit.hexsha]['message'] = commit.message.strip()
                commit_history[commit.hexsha]['parents'] = [parent.hexsha for parent in commit.parents]
                commit_history[commit.hexsha]['author'] = commit.author.name
                if 'branches' not in commit_history[commit.hexsha].keys():
                    commit_history[commit.hexsha]['branches'] = [branch.name]
                else:
                    commit_history[commit.hexsha]['branches'].append(branch.name)
        return commit_history

    print(commit_history_simple())


