//  messages modals logic
let alertAction = () => {
  $(".alert__popup").slideDown();
  setTimeout(() => {
    $(".alert__popup").slideUp();
  }, 2000);
};
