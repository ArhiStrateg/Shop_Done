$(document).ready(function() {
    $(document.getElementsByClassName("form-inline")).on('submit', function (e) {
        e.preventDefault();
        var id_modal = $(this).attr("id");
        var url = $(this).attr("action");

        var id_for_input = "input_" + id_modal;
        var imput_element = document.getElementById(id_for_input);
        var product_id = $(imput_element).attr("data-product_id_re");
        var name_in_form_target = $(imput_element).attr("name-in-form-target");
        var nmb = $(document.getElementById(id_for_input)).val();

        if (nmb > 0) {
            var csrf_token = $('[name="csrfmiddlewaretoken"]').val();
            var data = {};
            data.product_id = product_id;
            data.nmb = nmb;
            data["csrfmiddlewaretoken"] = csrf_token;

            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    if (data.product_total_nmb) {
                        $('#basket_total_nmb').text("(" + data.product_total_nmb + ")");
                    };
                }
            })
        };

        div_bloc = document.getElementById(name_in_form_target);

        $(function () {
            id_for_button = "button_" + id_modal;
            button_close = document.getElementById(id_for_button);
            $(button_close).trigger({ type: "click" });
            $(".modal-backdrop").hide();
            $(button_close).trigger({ type: "click" });
        });
        $("input.form-control").val('');

    });
});
