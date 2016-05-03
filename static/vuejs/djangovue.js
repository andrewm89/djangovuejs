Vue.config.delimiters = ["[[","]]"]

var demo = new Vue({
    el: '#app',
    data: {
        'apptitle': 'Django Job Board',
        'jobtitle': '',
        'jobdescription': '',
        'jobs': []
    },
    methods: {
        addJob: function () {
            var newJob = {}
            newJob.jobtitle = this.jobtitle.trim()
            newJob.jobdescription = this.jobdescription.trim()
            newJob.postdate = new Date()

            this.jobs.push(newJob)
            this.jobtitle = ''
            this.jobdescription = ''
        }
    }
});