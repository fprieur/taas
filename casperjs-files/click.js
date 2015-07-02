casper.test.begin('click tests', 1, function(test) {
    
    var x = require('casper').selectXPath;

    casper.start(casper.cli.get("url"), function() {
        this.click(x(casper.cli.get("id"))); 
    });
    
    casper.then(function() {
       test.assertEquals(this.getCurrentUrl(), casper.cli.get("expected_url"), "expected url is correct");
    });

    casper.run(function() {
        test.done()
    });
});
