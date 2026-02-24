/**
 * click.ru anti-fraud script
 */

(function() {
    var ref_url = document.referrer;
    if (
        ref_url.indexOf('yabs.yandex') !== -1 ||
        window.document.location.href.indexOf('utm_source=yandex') !== -1 ||
        window.document.location.href.indexOf('yclid=') !== -1
    ) {
        var iframe = document.createElement("iframe");
        iframe.style.display = 'none';
        iframe.setAttribute(
            "src",
            'https://af.click.ru/collect_stat_iframe.html' +
            '?referer=' + encodeURIComponent(ref_url) +
            '&url=' + encodeURIComponent(window.location.href) +
            '&utl=1'
        );

        if (!document.body) {
            document.addEventListener("DOMContentLoaded", function (event) {
                document.body.appendChild(iframe);
            });
        } else {
            document.body.appendChild(iframe);
        }
    }
})();
