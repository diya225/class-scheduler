$("input[type='button']").click(function(e){
    var Id =(e.target.getAttribute('data-value'))
    let Items = ['#Box1', '#Box2', '#Box3', '#Box4', '#Box5', '#Box6']
    let Index = parseInt(Items.indexOf(Id))
    let Ind = 0
    if(e.target.value === "next"){
        Ind = Index - 1
    }else{
        Ind = Index + 1
    }
    
    var empty = $(Items[Ind]).find("input[type='text'], input[type='date'], :checked").filter(function() {
        console.log("value is:", this.value)
        return this.value === "";
    });

    if(empty.length) {
        alert("Please fill all fields")
    }else{
        Items.map(function(item) {
            if(Id === item ) {
                $(item).addClass("active");
            }
            else {
            $(item).removeClass("active");
            }
        });
    }
});