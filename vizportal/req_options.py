from typing import List, Dict, Union

class VizportalRequestOptions:
    class Operator:
        Equals = "eq"
        GreaterThan = "gt"
        GreaterThanOrEqual = "gte"
        LessThan = "lt"
        LessThanOrEqual = "lte"
        In = "in"
        Has = "has"

    class Field:
        Args = "args"
        CompletedAt = "completedAt"
        CreatedAt = "createdAt"
        DomainName = "domainName"
        DomainNickname = "domainNickname"
        HitsTotal = "hitsTotal"
        IsLocal = "isLocal"
        JobType = "jobType"
        LastLogin = "lastLogin"
        MinimumSiteRole = "minimumSiteRole"
        Name = "name"
        Notes = "notes"
        OwnerDomain = "ownerDomain"
        OwnerEmail = "ownerEmail"
        OwnerName = "ownerName"
        ParentProjectId = "parentProjectId"
        Progress = "progress"
        ProjectName = "projectName"
        PublishSamples = "publishSamples"
        SiteRole = "siteRole"
        StartedAt = "startedAt"
        Status = "status"
        Subtitle = "subtitle"
        Tags = "tags"
        Title = "title"
        TopLevelProject = "topLevelProject"
        Type = "type"
        UpdatedAt = "updatedAt"
        UserCount = "userCount"
        HasAlert = "hasAlert"
        OwnerId = "ownerId"
        ServerName = "serverName"
        IsDefaultPort = "isDefaultPort"
        DatabaseUsername = "databaseUsername"
        HasEmbeddedPassword = "hasEmbeddedPassword"
        IsFavorite = "isFavorite"
        ExtractStatus = "extractStatus"
        IsCertified = "isCertified"
        IsPublished = "isPublished"
        WorkbookConnFilter = "workbookConnFilter"
        TopLevelProject = "topLevelProject"
        TaskType = "taskType"
        ContentType = "contentType"

    class Direction:
        Descending = "descending"
        Ascending = "ascending"

    class StatField:
        HitsTotal = "hitsTotal"
        FavoritesTotal = "favoritesTotal"
        HitsLastOneMonthTotal = "hitsLastOneMonthTotal"
        HitsLastThreeMonthsTotal = "hitsLastThreeMonthsTotal"
        HitsLastTwelveMonthsTotal = "hitsLastTwelveMonthsTotal"
        SubscriptionsTotal = "subscriptionsTotal"
        ConnectedWorkbooksCount = "connectedWorkbooksCount"

    class DatasourceType:
        Extract = "extract"
        Live = "live"
        LiveConnection = "liveConnection"

    class ContentType:
        Workbook = "workbook"
        Datasource = "datasource"
        Project = "project"
        View = "view"
        User = "user"
        Site = "site"
        Server = "server"
        Group = "group"
        Job = "job"
        Task = "task"
        DataRole = "dataRole"
        Lens = "lens"
        Flow = "flow"
        Metric = "metric"
        VirtualConnection = "virtualConnection"

    class TaskType:
        Extract = "extract"
        Refresh = "refresh"
        Schedule = "schedule"
        Subscription = "subscription"
        Sync = "sync"
        Webhook = "webhook"

    class SiteRole:
        Unlicensed = "Unlicensed"
        Guest = "Guest"
        Interactor = "Interactor"
        Explorer = "Explorer"
        Publisher = "Publisher"
        Creator = "Creator"
        Viewer = "Viewer"
        SiteAdministrator = "SiteAdministrator"
        SiteAdministratorCreator = "SiteAdministratorCreator"
        SiteAdministratorExplorer = "SiteAdministratorExplorer"
        SupportUser = "SupportUser"
        ServerAdministrator = "ServerAdministrator"
        ExplorerCanPublish = "ExplorerCanPublish"

    class DatasourceType:
        Live = "live"
        Published = "published"
        AllExtracts = "allExtracts"
        UnencryptedExtracts = "unencryptedExtracts"
        EncryptedExtracts = "encryptedExtracts"

class StatFieldBuilder:
    def __init__(self):
        self.stat_fields: list = []

    @staticmethod
    def default() -> List[str]:
        return [
            "hitsTotal",
            "favoritesTotal",
            "hitsLastOneMonthTotal",
            "hitsLastThreeMonthsTotal",
            "hitsLastTwelveMonthsTotal",
            "subscriptionsTotal",
        ]

    def add_stat_field(self, stat_field: str):
        self.stat_fields.append(stat_field)

    def add_stat_fields(self, stat_fields: List[str]):
        self.stat_fields.extend(stat_fields)

    def build(self) -> List[str]:
        return self.stat_fields


class FilterClauseBuilder:
    def __init__(self, operator: str = "and"):
        self.operator = operator
        self._clauses = []

    @property
    def clauses(self) -> Dict[str, Union[str, List[Dict[str, str]]]]:
        return {"operator": self.operator, "clauses": self._clauses}

    def add_clause(self, operator: str, field: str, value: str):
        self._clauses.append({"operator": operator, "field": field, "value": value})


class SortBuilder:
    def __init__(
        self, field: str = None, direction: str = None, sort_dict: Dict[str, str] = None
    ):
        self._sorts = []
        self.sort_dict = sort_dict
        self.field = field
        self.direction = direction

        # If field and direction are provided, add the sort.
        if field and direction:
            self.add_sort(field, direction)
        # If sort_dict is provided, add the sort.
        elif sort_dict and isinstance(sort_dict, dict):
            if sort_dict.get("field") and sort_dict.get("direction"):
                self.add_sort(sort_dict["field"], sort_dict["direction"])

    @property
    def sorts(self) -> List[Dict[str, Union[str, bool]]]:
        return self._sorts

    def add_sort(self, field: str, direction: str):
        if direction.lower() not in ["asc", "desc", "ascending", "descending"]:
            raise ValueError("Direction must be either 'asc', 'desc', 'ascending' or 'descending'.")

        self._sorts.append({"field": field, "ascending": direction.lower() in ["asc", "ascending"]})
