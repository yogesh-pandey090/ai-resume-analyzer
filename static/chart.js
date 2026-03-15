 function createChart(score){

const ctx = document.getElementById('chart');

new Chart(ctx,{
type:'doughnut',

data:{
labels:['Score','Remaining'],
datasets:[{
data:[score,100-score]
}]
}

})

}