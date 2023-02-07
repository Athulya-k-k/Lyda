  // ADD TO WISHLIST

  
(function ($) {
    "use strict";
    
        $('.plus-wishlist').click(function() { 
        var id=$(this).attr("pid").toString();
        console.log(id)
        $.ajax({
            type:"GET",
            url:"/wishlist/add_wishlist/",
            data:{
                prod_id:id
            },
            success:function(data) {
                swal.fire("Congratulations ! ", data.message, "success").then((value) => {

                    location.reload()
                    console.log(order_number)
                });
                
                
            }
        })

        });


        $('.minus-wishlist').click(function() { 
        var id=$(this).attr("pid").toString();
        $.ajax({
            type:"GET",
            url:"/wishlist/remove_wishlist",
            data:{
                prod_id:id
            },
            success:function(data) {
                swal.fire("Congratulations ! ", "Wishlist removed ", "success").then((value) => {

                    location.reload()
                    console.log(order_number)
                });
                
                
            }
        })

        });


})(jQuery);