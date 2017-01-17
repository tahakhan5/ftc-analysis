% eduomes
% Load edus
clear all
load('9.mat')

% create bins 0-30 30-40 40-50 50 >
cyber_bins = [0 0 0 0 0];

reg_bins = [0 0 0 0 0];

edu_tot = [0 0 0 0 0];


for n = 1:length(edu)
    
    
    if (edu(n) <= 10)
        cyber_bins(1) = cyber_bins(1) + cyber(n); reg_bins(1) = reg_bins(1) + reg(n);
        edu_tot(1) = edu_tot(1)+1;
    end
    
    if (edu(n) > 10 && edu(n) <= 20)
        cyber_bins(2) = cyber_bins(2) + cyber(n); reg_bins(2) = reg_bins(2) + reg(n);
        edu_tot(2) = edu_tot(2)+1;
    end
        
    if (edu(n) > 20 && edu(n) <= 50)
        cyber_bins(3) = cyber_bins(3) + cyber(n); reg_bins(3) = reg_bins(3) + reg(n);
        edu_tot(3) = edu_tot(3)+1;
    end 
    
    if (edu(n) > 50 && edu(n) <= 70)
        cyber_bins(4) = cyber_bins(4) + cyber(n); reg_bins(4) = reg_bins(4) + reg(n);
        edu_tot(4) = edu_tot(4)+1;
    end 
    
    if (edu(n) > 70)
        cyber_bins(5) = cyber_bins(5) + cyber(n); reg_bins(5) = reg_bins(5) + reg(n);
        edu_tot(5) = edu_tot(5)+1;
    end    
end

r =reg_bins./edu_tot
c= cyber_bins./edu_tot
x = [c;r]'
b = bar(x, 'r', 'EdgeColor',[0 0 0],'LineWidth',0.5, 'BarWidth', 0.5)
b(2).FaceColor = 'b';




axis([0.5 5.5 0 2.45])
labels = {'0-10','10-20','20-50','50-70','70+'};
set(gca, 'XTick', 1:5, 'XTickLabel', labels);
set(gca,'FontSize', 20);
xlabel({'College Education (%)';' ';'(c)'}', 'FontSize', 23)


ylabel({'Complaint Rate'}, 'FontSize', 23)
