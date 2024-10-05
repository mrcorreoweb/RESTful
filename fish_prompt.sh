function fish_prompt
    set_color purple
    echo -n (pwd)
    
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1
        set -l branch_name (git branch --show-current)
        set -l git_status (git status --porcelain)
        set -l unpushed (git log @{u}.. 2>/dev/null)
        set -l untracked (git ls-files --others --exclude-standard)
        
        if test -z "$git_status" -a -z "$unpushed" -a -z "$untracked"
            set_color green
        else
            set_color red
        end
        echo -n ' ('$branch_name')'
        
        set_color normal
        if test -n "$git_status"
            set -l staged (echo $git_status | grep -E '^[MADRC]')
            set -l unstaged (echo $git_status | grep -E '^.[MADRC]')
            if test -n "$staged"
                set_color yellow
                echo -n '+'
            end
            if test -n "$unstaged"
                set_color red
                echo -n '*'
            end
        end
        if test -n "$untracked"
            set_color cyan
            echo -n '?'
        end
        if test -n "$unpushed"
            set_color blue
            echo -n '↑'
        end
    end
    
    set_color normal
    echo -n ' > '
end