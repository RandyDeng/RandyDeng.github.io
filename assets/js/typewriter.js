var TxtRotate = function (el, job) {
    this.job = job;
    this.el = el;
    this.txt = '';
    this.tick();
};

TxtRotate.prototype.tick = function () {
    this.txt = this.job.substring(0, this.txt.length + 1);
    this.el.innerHTML = '<span class="wrap">' + this.txt + '</span>';

    if (!(this.txt === this.job)) {
        var that = this;
        setTimeout(function () {
            that.tick();
        }, 100);
    }
};

window.onload = function () {
    var elements = document.getElementsByClassName('typewriter')[0];
    var job = elements.getAttribute('job');
    new TxtRotate(elements, job);
};