odoo.define('delivery_time.checkout', function (require) {
    'use strict';
    var ajax = require('web.ajax');
    var core = require('web.core');
    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var _t = core._t;
    var concurrency = require('web.concurrency');
    var dp = new concurrency.DropPrevious();
    $(document).ready(function () {
        // ajax.jsonRpc('/shop/customer_order_date', 'call', {
        //     'delivery_time': customer_order_delivery_date,
        // });
        ajax.jsonRpc('/warehouse/get_all', 'call', {}).then(function (result) {
                // $('select[name="av_time"]').empty();
                // document.getElementById("times").innerHTML = "";
                // document.getElementById("deliver_times").style.display = "block"
            console.log(result);
            console.log(result[0].id);
            // $modal = $(result);
            // console.log($modal);
                for (var i = 0; i < result.length; i++) {
                    $('select[name="warehouse"]').append("<option t-att-value='" + result[i].id + "'  t-att-id='" + result[i].id + "'>" + result[i].name + "</option>");
               

                }


            });
        
    });
    // publicWidget.registry.websiteSaleDelivery = publicWidget.Widget.extend({
    //     selector: '.oe_website_sale',
    //     events: {
    //         'change select[name="av_day2"]': '_onchangedate',
    //         'change input[name="delivery_type"]': '_onchangetime',
    //     },



    //     //--------------------------------------------------------------------------
    //     // Handlers
    //     //--------------------------------------------------------------------------


    //     /**
    //      * @privatec
    //      * @param {Event} ev
    //      */
    //     _onchangedate: function (ev) {
    //         var value = $(ev.currentTarget).val();
    //         var warehouse = document.getElementById("customer_warehouse").innerHTML;
    //         var self = this;
    //         var av_times = $('select[name="av_time"]');
    //         if (value != "As Soon As Possible") {
    //             this._rpc({
    //                 model: 'res.partner',
    //                 method: 'get_available_times',
    //                 args: [parseInt(warehouse), value],
    //             })
    //                 .then(function (result) {
    //                     // $('select[name="av_time"]').empty();
    //                     document.getElementById("times").innerHTML = "";
    //                     document.getElementById("deliver_times").style.display = "block"
    //                     for (var i = 0; i < result.length; i++) {
    //                         //   $('select[name="av_time"]').append("<option t-att-value='val'>"+result[i] +"</option>");
    //                         document.getElementById("times").innerHTML += '<section class="main-content delivery-time-section"><div class="rounded-top"><div class="container"><div class="delivery-time-options form-group"><div class="form-check"><input class="form-check-input" t-att-value="' + result[i] + '" t-att-id="' + result[i] + '" type="radio" name="timeOptions" id="option' + [i] + '" /><label class="form-check-label text-align-left" for="option' + [i] + '" dir="ltr" />' + result[i] + '</div></div></div></div></section>';


    //                     }


    //                 });
    //         }
    //         else {
    //             $('select[name="av_time"]').empty();
    //             document.getElementById("deliver_times").style.display = "none"
    //         }

    //     },
    //     _onchangetime: function (ev) {

    //         console.log($('input[name="delivery_type"]:checked').val());
    //     },
    // });
});
