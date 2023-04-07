class Endpoints:
    """Endpoints for the Vizportal API"""

    class Get:
        """Endpoints for GET requests"""

        Workbooks = "getWorkbooks"
        Workbook = "getWorkbook"
        Datasource = "getDatasource"
        Datasources = "getDatasources"
        Projects = "getProjects"
        User = "getUser"
        Users = "getUsers"
        Group = "getGroup"
        Groups = "getGroups"
        View  = "getView"
        Views = "getViews"
        Favorites = "getFavorites"
        Flow = "getFlow"
        Flows = "getFlows"
        Metrics = "getMetrics"
        Schedule = "getSchedule"
        Schedules = "getSchedules"
        Lenses = "getLenses"
        Subscriptions = "getSubscriptions"
        DataRoles = "getDataRoles"
        DetailedRecents = "getDetailedRecents"
        Recommendations = "getRecommendations"
        DataConnections = "getDataConnections"
        BackgroundJobs = "getBackgroundJobs"
        ContentForUser = "getContentForUser"
        PersonalAccessTokenNames = "getPersonalAccessTokenNames"
        SiteUsers = "getSiteUsers"
        UsersGroupMembership = "getUsersGroupMembership"
        Sites = "getSites"
        Site = "getSite"
        Task = "getTask"
        Tasks = "getTasks"
        Webhook = "getWebhook"
        Webhooks = "getWebhooks"
        Alert = "getAlert"
        Alerts = "getAlerts"
        ViewByPath = "getViewByPath"
        ViewActions = "getViewActions"
        UsersGroupMembership = "getUsersGroupMembership"
        Tags = "getTags"
        ExplicitPermissions = "getExplicitPermissions"
        UserSettings = "getUserSettings"
        SiteSettings = "getSiteSettings"
        ServerSettings = "getServerSettings"
        ServerInfo = "getServerInfo"
        ServerVersion = "getServerVersion"
        ServerStatus = "getServerStatus"
        ProjectActions = "getProjectActions"
        Project = "getProject"
        ProjectNames = "getProjectNames"
        ProjectPermissions = "getProjectPermissions"
        LastActiveDirectoryGroupSyncTime = "getLastActiveDirectoryGroupSyncTime"
        Comments = "getComments"



    class Update:
        """Endpoints for UPDATE requests"""

        Workbook = "updateWorkbook"
        Datasource = "updateDatasource"
        Project = "updateProject"
        Group = "updateGroup"
        User = "updateUser"
        Site = "updateSite"
        Flow = "updateFlow"
        UserStartPage = "updateUserStartPage"
        UserGroupMembership = "updateUserGroupMembership"
        UsersSiteRole = "updateUsersSiteRole"
        UserEmail = "updateUserEmail"
        ProjectDescription = "updateProjectDescription"
        ProjectOwner = "updateProjectOwner"
        ProjectParent = "updateProjectParent"
        ProjectTags = "updateProjectTags"
        ProjectPermissions = "updateProjectPermissions"
        Connections = "updateConnections"


    class Create:
        """Endpoints for CREATE requests"""

        CreateProject = "createProject"
        CreateGroup = "createGroup"
        CreateUser = "createUser"
        PublishWorkbook = "publishWorkbook"
        PublishDatasource = "publishDatasource"
        PublishFlow = "publishFlow"
        PublicKey = "generatePublicKey"
        Commonet = "createComment"

    class Delete:
        """Endpoints for DELETE requests"""

        WorkbookVersions = "deleteWorkbookVersions"
        UserRefreshTokens = "deleteUserRefreshTokens"
        TagsFromWorkbooks = "removeTagsFromWorkbooks"
        Comment = "deleteComment"

    class Move:
        """Endpoints for MOVE requests"""

        MoveWorkbooksToProject = "moveWorkbooksToProject"

    class Set:
        """Endpoints for SET requests"""

        WorkbooksOwner = "setWorkbooksOwner"
        WorkbookDescription = "setWorkbookDescription"
        DisplayTabs = "setDisplayTabs"

    class Others:
        CheckConnection = "checkConnection"        
