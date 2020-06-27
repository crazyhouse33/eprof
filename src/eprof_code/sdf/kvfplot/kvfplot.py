import parser
import bcolors

def get_git_file(file,commit):
    print("Recolting commit ", bcolors.BOLD,commit.hexsha,":", commit.message, bcolors.ENDC)

args= parser.getArgs()

file = args["file"]
sep_key = args["sep_key"] 
sep_val=args["sep_val"
keys=args["keys"]
branch= args["branch"]

if not args['git']:

    sdf= Serie_dict_file(file, sep_key, sep_val])
    sdf.plot_pie(keys)
else:

    import git
    import pydriller

    breakpoint()
    repo = git.Repo(file, search_parent_directories=True).working_dir
    if branch==None:
        branch = repo.active_branch 
    

for commit in RepositoryMining(repo, only_in_branch=branch, only_commits = commits, filepath=file).traverse_commits():
    commit.modifications


    for commit in commits:






