

function showCategory(){
  $.ajax({
    type: "GET",
    url: "/topics/category",
    success: function(data) {
      side_bar = $("#side-bar-category");
      side_bar.empty();
      side_bar.append(data);
    },
    error: function(req, sts, err) {
      alert("Error! sts=" + sts);
    }
  });
}

function showTopicLine(category_cd){
  $.ajax({
    type: "GET",
    url: "/topics/line/"+category_cd,
    success: function(data) {
      topicline = $("#topic-line");
      topicline.empty();
      topicline.append(data);
    },
    error: function(req, sts, err) {
      alert("Error! sts=" + sts);
    }
  });
}

function showTopicDetail(topic_id){
  $.ajax({
    type: "GET",
    url: '/topics/detail/'+topic_id,
    success: function(data) {
      topicdetail = $("#topic-detail");
      topicdetail.empty();
      topicdetail.append(data);
    },
    error: function(req, sts, err) {
      alert("Error! sts=" + sts);
    }
  });
}

function showAll(){
  $(".tfidf").show();
}

function openTfidf(id){;
  $("#"+id).show();
}
function closeTfidf(id){
  $("#"+id).hide();
}
