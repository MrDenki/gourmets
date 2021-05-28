function SendComment(obj, id) {
    let comment = $("#comment").val()
    if (comment != '') {
        $.ajax({
            url: '/comment/',
            type: 'POST',
            data: {
                'comment': comment,
                'id': id
            },
            success: function (response) {
                $('.print-comments').append('<div>\n' +
                    '                            <h4 style="font-family: Roboto; margin-left: 1%; margin-right: 1%; ">'+response['user']+'</h4>\n' +
                    '                            <p style="font-family: Roboto; margin-left: 1%; margin-right: 1%;">'+response['content']+'</p>\n' +
                    '                        </div>')
                $("#comment").val('')
            }
        })
    }
}