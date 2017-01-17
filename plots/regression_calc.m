Y = double(reg_ds(:,2:end));
[n,d] = size(Y);
x = reg_ds.reg;

% figure;
% regions = reg_ds.Properties.VarNames(2:end);
% plot(x,Y,'x')
% legend(regions,'Location','NorthWest')

X = cell(n,1);
for i=1:n
		X{i} = [eye(d) repmat(x(i),d,1)];
end

[beta,Sigma] = mvregress(X,Y);


B = [beta(1:d)';repmat(beta(end),1,d)];


xx = linspace(.5,100000)';

fits = [ones(size(xx)),xx]*B;
% 
figure;
h = plot(xx,fits,'-');
% 
% 
% 
% for i = 1:d
% 	set(h(d+i),'color',get(h(i),'color'));
% end
% legend(regions,'Location','NorthWest');






