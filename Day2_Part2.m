inp = importdata('Day2_1.txt');
right_pwd = 0;

for i = 1:length(inp)
    pwd = cell2mat(inp(i));
    for j = 1:length(pwd)
        idx_hyph = strfind(pwd,'-');
        idx_space = strfind(pwd,' ');
        pos1 = str2num(strcat(pwd(1:idx_hyph-1)));
        pos2 = str2num(strcat(pwd((idx_hyph+1):(idx_space(1)-1))));
        letter = pwd(idx_space(1)+1);
        letter_count = 0;
        comp1 = idx_space(2)+pos1;
        comp2 = idx_space(2)+pos2;
        if(strcmp(pwd(comp1),letter)==1) && (strcmp(pwd(comp2),letter)==1)
            letter_count = 0;
        elseif(strcmp(pwd(comp1),letter)==0) && (strcmp(pwd(comp2),letter)==0)
            letter_count = 0;
        else
            letter_count = letter_count+1;
        end
    end
            if (letter_count~=0)
            right_pwd = right_pwd+1;
            end
end
      

     
