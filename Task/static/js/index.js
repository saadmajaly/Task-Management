function handleClick(event) {
      var title = event.target.nextElementSibling;
      if (event.target.checked) {
        title.style.textDecoration = "line-through";
        title.style.fontWeight = "normal";
        title.style.color = "#413a3a";
      } else {
        title.style.textDecoration = "none";
        title.style.fontWeight = "bold";
        title.style.color = "black";
      }
    }

    function handleSorting() {
      var val = document.getElementById("sort").value;
      console.log(val);
      window.location = val;
    }