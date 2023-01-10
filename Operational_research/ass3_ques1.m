%% M ax. z = x1 + 2x2, 
%%subject to − x1 + x2 ≤ 1, x1 + x2 ≤ 2, 
%%x1, x2 ≥ 0.


clc
clear all
format short
noofvariables=2;

c = [1 2]
a = [-1 1; 1 1]
b = [1;2]
s= eye(size(a,1));
A = [a s b]
cost = zeros(1,size(A,2));
cost(1:noofvariables)=c;
bv = noofvariables+1:size(A,2)-1;
zjcj = cost(bv)*A -cost;
zcj = [zjcj; A];
simptable = array2table(zcj)
simptable.Properties.VariableNames(1:size(zcj,2))= {'x_1','x_2','s1','s2','b'}

run = true;
while(run)
    zc=zjcj(1:end-1);
    if any(zc<0);
            fprintf('bfs is not optimal')
            [Enter_val,pvt_col]=min(zc)
            if all(A(:,pvt_col)<=0)
                error('lpp is unbounded')
            else
                sol = A(:,end)

                col= A(:,pvt_col)
                for i=1:size(A,1)
                    if(col(i)>0)
                        ratio(i)=sol(i)/col(i)

                    else
                        ratio(i) = inf

                    end
                end
                [leaving_variable,pvt_row]=min(ratio)
            end
    
        pvt_key = A(pvt_row, pvt_col)
        bv(pvt_row) = pvt_col
        A(pvt_row,:)=A(pvt_row,:)/pvt_key

        for i=1:size(A,1)
            if i~= pvt_row
                A(i,:)= A(i,:)- A(i,pvt_col).*A(pvt_row,:)
            end
        end
        zjcj = zjcj - zjcj(pvt_col).* A(pvt_row,:)
        zcj1=[zjcj;A]
        table = array2table(zcj1)
        table.Properties.VariableNames(1:size(zcj1,2))= {'x_1','x_2','s1','s2','b'}

        BFS=zeros(1,size(A,2));
        BFS(bv)=A(:,end);
        BFS(end)=sum(BFS.*cost);
        CurrentBFS=array2table(BFS);
        CurrentBFS.Properties.VariableNames(1:size(CurrentBFS,2))={'x1','x2','s1','s2','Sol'}

    else
        run = false;
        fprintf("the current bfs is optimal")

    end
 end