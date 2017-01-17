% Load Ages
clear all
load('7.mat')

% create bins 0-30 30-40 40-50 50 >
cyber_bins = [0 0 0 0 0];

reg_bins = [0 0 0 0 0];

age_tot = [0 0 0 0 0];


for n = 1:length(age)
    
    
    if (age(n) <= 30)
        cyber_bins(1) = cyber_bins(1) + cyber(n); reg_bins(1) = reg_bins(1) + reg(n);
        age_tot(1) = age_tot(1)+1;
    end
    
    if (age(n) > 30 && age(n) <= 40)
        cyber_bins(2) = cyber_bins(2) + cyber(n); reg_bins(2) = reg_bins(2) + reg(n);
        age_tot(2) = age_tot(2)+1;
    end
        
    if (age(n) > 40 && age(n) <= 45)
        cyber_bins(3) = cyber_bins(3) + cyber(n); reg_bins(3) = reg_bins(3) + reg(n);
        age_tot(3) = age_tot(3)+1;
    end 
    
    if (age(n) > 45 && age(n) <= 50)
        cyber_bins(4) = cyber_bins(4) + cyber(n); reg_bins(4) = reg_bins(4) + reg(n);
        age_tot(4) = age_tot(4)+1;
    end 
    
    if (age(n) > 50)
        cyber_bins(5) = cyber_bins(5) + cyber(n); reg_bins(5) = reg_bins(5) + reg(n);
        age_tot(5) = age_tot(5)+1;
    end    
end

r= reg_bins./age_tot
c = cyber_bins./age_tot
x = [c;r]'
b = bar(x, 'r', 'EdgeColor',[0 0 0],'LineWidth',0.5, 'BarWidth', 0.5)
b(2).FaceColor = 'b';



axis([0.5 5.5 0 4])
labels = {'0-30','30-40','40-45','46-50','50+'};
set(gca, 'XTick', 1:5, 'XTickLabel', labels);
set(gca,'FontSize', 20);
xlabel({'Ages';' ';'(a)'}', 'FontSize', 23)


ylabel({'Fraud Rate'}, 'FontSize', 23)



