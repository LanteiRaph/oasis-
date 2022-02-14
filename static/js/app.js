window.addEventListener("load", () => {
  //Get all the document objects to manupilate
  const is_student = document.querySelector("#type");
  //Change the ui to refeclet the
  const student_data = document.querySelector("#student_data");
  //Add on change event to handle the user inaractions
  is_student.addEventListener("change", () => {
    //Get the value of the slected choice
    var strUser = is_student.options[is_student.selectedIndex].value;
    if (strUser == "yes") {
      //Change the display
      student_data.style.display = "block";
    } else {
        //Set display to none.
        student_data.style.display = 'none'
    }
  });
});
