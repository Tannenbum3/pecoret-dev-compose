export default class AdminService {
    getUsers(api, params){
        let url = "/users/"
        let config = {}
        if (params){
            config["params"] = params
        }
        return api.get(url, config)
    }

    deleteUser(api, userId){
        let url = "/users/" + userId + "/"
        return api.delete(url)
    }

    createUser(api, data){
        let url = "/users/"
        return api.post(url, data)
    }
    
    patchUser(api, userId, data){
        let url = "/users/" + userId + "/"
        return api.patch(url, data)
    }

    getGroups(api){
        let url = "/groups/"
        return api.get(url)
    }


    deleteReportTemplate(api, templateId){
        let url = "/report-templates/" + templateId + "/"
        return api.delete(url)
    }

    getReportTemplates(api){
        let url = "/report-templates/"
        return api.get(url)
    }

    patchReportTemplate(api, templateId, data){
        let url = "/report-templates/" + templateId + "/"
        return api.patch(url, data)
    }

    createReportTemplate(api, data){
        let url = "/report-templates/"
        return api.post(url, data)
    }

    getProjectTypes(api, params){
        let url = "/pentest-types/"
        let config = {}
        if (params){
            config["params"] = params
        }
        return api.get(url, config)
    }

    deleteProjectType(api, id){
        let url = "/pentest-types/" + id + "/"
        return api.delete(url)
    }

    patchProjectType(api, id, data){
        let url = "/pentest-types/" + id + "/"
        return api.patch(url, data)
    }

    createProjectType(api, data){
        let url = "/pentest-types/"
        return api.post(url, data)
    }
}