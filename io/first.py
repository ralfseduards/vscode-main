
# f = open("/workspaces/vscode/io/test.txt", "r")
# f.close()

open("/workspaces/vscode/io/test.txt", "r") as rf: # best practice - file closes after this block
open("/workspaces/vscode/io/test_copy.txt", "w") as wf:
        for line in rf:
            print(line)
            wf.write(line)
