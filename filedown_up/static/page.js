/**
 * 分页函数
 * pno--页数
 * psize--每页显示记录数
 * 分页部分是从真实数据行开始，因而存在加减某个常数，以确定真正的记录数
 * 纯js分页实质是数据行全部加载，通过是否显示属性完成分页功能
 **/
function goPage(pno,psize){
    var itable = document.getElementById("idData_tbody");
    var num = itable.rows.length;//表格所有行数(所有记录数)
    console.log(num);
    var totalPage = 0;//总页数
    var pageSize = psize;//每页显示行数
    //总共分几页 
    if(num/pageSize > parseInt(num/pageSize)){   
            totalPage=parseInt(num/pageSize)+1;   
       }else{   
           totalPage=parseInt(num/pageSize);   
       }   
    var currentPage = pno;//当前页数
    var startRow = (currentPage - 1) * pageSize+1;//开始显示的行  31 
       var endRow = currentPage * pageSize;//结束显示的行   40
       endRow = (endRow > num)? num : endRow;    40
       console.log(endRow);
       //遍历显示数据实现分页
    for(var i=1;i<(num+1);i++){    
        var irow = itable.rows[i-1];
        if(i>=startRow && i<=endRow){
            irow.style.display = "table-row";
        }else{
            irow.style.display = "none";
        }
    }
    var pageEnd = document.getElementById("pageEnd");
    var tempStr = "&nbsp;&nbsp;共"+num+"条记录 分"+totalPage+"页 当前第"+currentPage+"页 ";
    if(currentPage>1){
        tempStr += "<br><br><a href=\"#\" onClick=\"goPage("+(1)+","+psize+")\">首页 </a>&nbsp;";
        tempStr += "&nbsp;&nbsp;<a href=\"#\" onClick=\"goPage("+(currentPage-1)+","+psize+")\"><上一页 </a>&nbsp;"
    }else{
        tempStr += "<br><br>首页 ";
        tempStr += "&nbsp;&nbsp;<上一页 ";    
    }

    if(currentPage<totalPage){
        tempStr += "&nbsp;<a href=\"#\" onClick=\"goPage("+(currentPage+1)+","+psize+")\">下一页> </a>&nbsp; ";
        tempStr += "&nbsp;<a href=\"#\" onClick=\"goPage("+(totalPage)+","+psize+")\">尾页</a>&nbsp;";
    }else{
        tempStr += "&nbsp;下一页> ";
        tempStr += "&nbsp;尾页";    
    }

    document.getElementById("barcon").innerHTML = tempStr;
    
}