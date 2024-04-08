inp = importdata('Day2_1.txt');
right_pwd = 0;

for i = 1:length(inp)
    pwd = cell2mat(inp(i));
    for j = 1:length(pwd)
        idx_hyph = strfind(pwd,'-');
        idx_space = strfind(pwd,' ');
        min = str2num(strcat(pwd(1:idx_hyph-1)));
        max = str2num(strcat(pwd((idx_hyph+1):(idx_space(1)-1))));
        letter = pwd(idx_space(1)+1);
        letter_count = 0;
        for k = (idx_space(2)+1):length(pwd)
            if(strcmp(pwd(k),letter) == 1)
                letter_count = letter_count + 1; 
            end
        end

    end
            if (letter_count>=min && letter_count<=max)
            right_pwd = right_pwd+1;
            end
end
      

     
