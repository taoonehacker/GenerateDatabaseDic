#### __efmigrationshistory 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | MigrationId | varchar(95) | None |  | 
  | 2 | ProductVersion | varchar(32) | None |  | 
 #### abpauditlogs 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | TenantId | int | None |  | 
  | 3 | UserId | bigint | None |  | 
  | 4 | ServiceName | varchar(256) | None |  | 
  | 5 | MethodName | varchar(256) | None |  | 
  | 6 | Parameters | varchar(1024) | None |  | 
  | 7 | ReturnValue | longtext | None |  | 
  | 8 | ExecutionTime | datetime(6) | None |  | 
  | 9 | ExecutionDuration | int | None |  | 
  | 10 | ClientIpAddress | varchar(64) | None |  | 
  | 11 | ClientName | varchar(128) | None |  | 
  | 12 | BrowserInfo | varchar(512) | None |  | 
  | 13 | Exception | varchar(2000) | None |  | 
  | 14 | ImpersonatorUserId | bigint | None |  | 
  | 15 | ImpersonatorTenantId | int | None |  | 
  | 16 | CustomData | varchar(2000) | None |  | 
 #### abpbackgroundjobs 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | JobType | varchar(512) | None |  | 
  | 5 | JobArgs | longtext | None |  | 
  | 6 | TryCount | smallint | None |  | 
  | 7 | NextTryTime | datetime(6) | None |  | 
  | 8 | LastTryTime | datetime(6) | None |  | 
  | 9 | IsAbandoned | tinyint(1) | None |  | 
  | 10 | Priority | tinyint unsigned | None |  | 
 #### abpdynamicparameters 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | ParameterName | varchar(255) | None |  | 
  | 3 | InputType | longtext | None |  | 
  | 4 | Permission | longtext | None |  | 
  | 5 | TenantId | int | None |  | 
 #### abpdynamicparametervalues 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Value | longtext | None |  | 
  | 3 | TenantId | int | None |  | 
  | 4 | DynamicParameterId | int | None |  | 
 #### abpeditions 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | IsDeleted | tinyint(1) | None |  | 
  | 7 | DeleterUserId | bigint | None |  | 
  | 8 | DeletionTime | datetime(6) | None |  | 
  | 9 | Name | varchar(32) | None |  | 
  | 10 | DisplayName | varchar(64) | None |  | 
  | 11 | Discriminator | longtext | None |  | 
  | 12 | ExpiringEditionId | int | None |  | 
  | 13 | DailyPrice | decimal(65,30) | None |  | 
  | 14 | WeeklyPrice | decimal(65,30) | None |  | 
  | 15 | MonthlyPrice | decimal(65,30) | None |  | 
  | 16 | AnnualPrice | decimal(65,30) | None |  | 
  | 17 | TrialDayCount | int | None |  | 
  | 18 | WaitingDayAfterExpire | int | None |  | 
 #### abpentitychanges 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | ChangeTime | datetime(6) | None |  | 
  | 3 | ChangeType | tinyint unsigned | None |  | 
  | 4 | EntityChangeSetId | bigint | None |  | 
  | 5 | EntityId | varchar(48) | None |  | 
  | 6 | EntityTypeFullName | varchar(192) | None |  | 
  | 7 | TenantId | int | None |  | 
 #### abpentitychangesets 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | BrowserInfo | varchar(512) | None |  | 
  | 3 | ClientIpAddress | varchar(64) | None |  | 
  | 4 | ClientName | varchar(128) | None |  | 
  | 5 | CreationTime | datetime(6) | None |  | 
  | 6 | ExtensionData | longtext | None |  | 
  | 7 | ImpersonatorTenantId | int | None |  | 
  | 8 | ImpersonatorUserId | bigint | None |  | 
  | 9 | Reason | varchar(256) | None |  | 
  | 10 | TenantId | int | None |  | 
  | 11 | UserId | bigint | None |  | 
 #### abpentitydynamicparameters 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | EntityFullName | varchar(255) | None |  | 
  | 3 | DynamicParameterId | int | None |  | 
  | 4 | TenantId | int | None |  | 
 #### abpentitydynamicparametervalues 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Value | longtext | None |  | 
  | 3 | EntityId | longtext | None |  | 
  | 4 | EntityDynamicParameterId | int | None |  | 
  | 5 | TenantId | int | None |  | 
 #### abpentitypropertychanges 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | EntityChangeId | bigint | None |  | 
  | 3 | NewValue | varchar(512) | None |  | 
  | 4 | OriginalValue | varchar(512) | None |  | 
  | 5 | PropertyName | varchar(96) | None |  | 
  | 6 | PropertyTypeFullName | varchar(192) | None |  | 
  | 7 | TenantId | int | None |  | 
 #### abpfeatures 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | TenantId | int | None |  | 
  | 5 | Name | varchar(128) | None |  | 
  | 6 | Value | varchar(2000) | None |  | 
  | 7 | Discriminator | longtext | None |  | 
  | 8 | EditionId | int | None |  | 
 #### abplanguages 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | IsDeleted | tinyint(1) | None |  | 
  | 7 | DeleterUserId | bigint | None |  | 
  | 8 | DeletionTime | datetime(6) | None |  | 
  | 9 | TenantId | int | None |  | 
  | 10 | Name | varchar(128) | None |  | 
  | 11 | DisplayName | varchar(64) | None |  | 
  | 12 | Icon | varchar(128) | None |  | 
  | 13 | IsDisabled | tinyint(1) | None |  | 
 #### abplanguagetexts 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | TenantId | int | None |  | 
  | 7 | LanguageName | varchar(128) | None |  | 
  | 8 | Source | varchar(128) | None |  | 
  | 9 | Key | varchar(256) | None |  | 
  | 10 | Value | longtext | None |  | 
 #### abpnotifications 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | char(36) | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | NotificationName | varchar(96) | None |  | 
  | 5 | Data | longtext | None |  | 
  | 6 | DataTypeName | varchar(512) | None |  | 
  | 7 | EntityTypeName | varchar(250) | None |  | 
  | 8 | EntityTypeAssemblyQualifiedName | varchar(512) | None |  | 
  | 9 | EntityId | varchar(96) | None |  | 
  | 10 | Severity | tinyint unsigned | None |  | 
  | 11 | UserIds | longtext | None |  | 
  | 12 | ExcludedUserIds | longtext | None |  | 
  | 13 | TenantIds | longtext | None |  | 
 #### abpnotificationsubscriptions 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | char(36) | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | TenantId | int | None |  | 
  | 5 | UserId | bigint | None |  | 
  | 6 | NotificationName | varchar(96) | None |  | 
  | 7 | EntityTypeName | varchar(250) | None |  | 
  | 8 | EntityTypeAssemblyQualifiedName | varchar(512) | None |  | 
  | 9 | EntityId | varchar(96) | None |  | 
 #### abporganizationunitroles 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | TenantId | int | None |  | 
  | 5 | RoleId | int | None |  | 
  | 6 | OrganizationUnitId | bigint | None |  | 
  | 7 | IsDeleted | tinyint(1) | None |  | 
 #### abporganizationunits 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | IsDeleted | tinyint(1) | None |  | 
  | 7 | DeleterUserId | bigint | None |  | 
  | 8 | DeletionTime | datetime(6) | None |  | 
  | 9 | TenantId | int | None |  | 
  | 10 | ParentId | bigint | None |  | 
  | 11 | Code | varchar(95) | None |  | 
  | 12 | DisplayName | varchar(128) | None |  | 
 #### abppermissions 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | TenantId | int | None |  | 
  | 5 | Name | varchar(128) | None |  | 
  | 6 | IsGranted | tinyint(1) | None |  | 
  | 7 | Discriminator | longtext | None |  | 
  | 8 | RoleId | int | None |  | 
  | 9 | UserId | bigint | None |  | 
 #### abppersistedgrants 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | varchar(200) | None |  | 
  | 2 | Type | varchar(50) | None |  | 
  | 3 | SubjectId | varchar(200) | None |  | 
  | 4 | ClientId | varchar(200) | None |  | 
  | 5 | CreationTime | datetime(6) | None |  | 
  | 6 | Expiration | datetime(6) | None |  | 
  | 7 | Data | longtext | None |  | 
 #### abproleclaims 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | TenantId | int | None |  | 
  | 5 | RoleId | int | None |  | 
  | 6 | ClaimType | varchar(256) | None |  | 
  | 7 | ClaimValue | longtext | None |  | 
 #### abproles 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | IsDeleted | tinyint(1) | None |  | 
  | 7 | DeleterUserId | bigint | None |  | 
  | 8 | DeletionTime | datetime(6) | None |  | 
  | 9 | TenantId | int | None |  | 
  | 10 | Name | varchar(32) | None |  | 
  | 11 | DisplayName | varchar(64) | None |  | 
  | 12 | IsStatic | tinyint(1) | None |  | 
  | 13 | IsDefault | tinyint(1) | None |  | 
  | 14 | NormalizedName | varchar(32) | None |  | 
  | 15 | ConcurrencyStamp | varchar(128) | None |  | 
 #### abpsettings 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | TenantId | int | None |  | 
  | 7 | UserId | bigint | None |  | 
  | 8 | Name | varchar(256) | None |  | 
  | 9 | Value | longtext | None |  | 
 #### abptenantnotifications 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | char(36) | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | TenantId | int | None |  | 
  | 5 | NotificationName | varchar(96) | None |  | 
  | 6 | Data | longtext | None |  | 
  | 7 | DataTypeName | varchar(512) | None |  | 
  | 8 | EntityTypeName | varchar(250) | None |  | 
  | 9 | EntityTypeAssemblyQualifiedName | varchar(512) | None |  | 
  | 10 | EntityId | varchar(96) | None |  | 
  | 11 | Severity | tinyint unsigned | None |  | 
 #### abptenants 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | IsDeleted | tinyint(1) | None |  | 
  | 7 | DeleterUserId | bigint | None |  | 
  | 8 | DeletionTime | datetime(6) | None |  | 
  | 9 | TenancyName | varchar(64) | None |  | 
  | 10 | Name | varchar(128) | None |  | 
  | 11 | ConnectionString | varchar(1024) | None |  | 
  | 12 | IsActive | tinyint(1) | None |  | 
  | 13 | EditionId | int | None |  | 
  | 14 | SubscriptionEndDateUtc | datetime(6) | None |  | 
  | 15 | IsInTrialPeriod | tinyint(1) | None |  | 
  | 16 | CustomCssId | char(36) | None |  | 
  | 17 | LogoId | char(36) | None |  | 
  | 18 | LogoFileType | varchar(64) | None |  | 
  | 19 | SubscriptionPaymentType | int | None |  | 
 #### abpuseraccounts 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | IsDeleted | tinyint(1) | None |  | 
  | 7 | DeleterUserId | bigint | None |  | 
  | 8 | DeletionTime | datetime(6) | None |  | 
  | 9 | TenantId | int | None |  | 
  | 10 | UserId | bigint | None |  | 
  | 11 | UserLinkId | bigint | None |  | 
  | 12 | UserName | varchar(256) | None |  | 
  | 13 | EmailAddress | varchar(256) | None |  | 
 #### abpuserclaims 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | TenantId | int | None |  | 
  | 5 | UserId | bigint | None |  | 
  | 6 | ClaimType | varchar(256) | None |  | 
  | 7 | ClaimValue | longtext | None |  | 
 #### abpuserloginattempts 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | TenantId | int | None |  | 
  | 3 | TenancyName | varchar(64) | None |  | 
  | 4 | UserId | bigint | None |  | 
  | 5 | UserNameOrEmailAddress | varchar(256) | None |  | 
  | 6 | ClientIpAddress | varchar(64) | None |  | 
  | 7 | ClientName | varchar(128) | None |  | 
  | 8 | BrowserInfo | varchar(512) | None |  | 
  | 9 | Result | tinyint unsigned | None |  | 
  | 10 | CreationTime | datetime(6) | None |  | 
 #### abpuserlogins 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | TenantId | int | None |  | 
  | 3 | UserId | bigint | None |  | 
  | 4 | LoginProvider | varchar(128) | None |  | 
  | 5 | ProviderKey | varchar(256) | None |  | 
 #### abpusernotifications 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | char(36) | None |  | 
  | 2 | TenantId | int | None |  | 
  | 3 | UserId | bigint | None |  | 
  | 4 | TenantNotificationId | char(36) | None |  | 
  | 5 | State | int | None |  | 
  | 6 | CreationTime | datetime(6) | None |  | 
 #### abpuserorganizationunits 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | TenantId | int | None |  | 
  | 5 | UserId | bigint | None |  | 
  | 6 | OrganizationUnitId | bigint | None |  | 
  | 7 | IsDeleted | tinyint(1) | None |  | 
 #### abpuserroles 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | TenantId | int | None |  | 
  | 5 | UserId | bigint | None |  | 
  | 6 | RoleId | int | None |  | 
 #### abpusers 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | IsDeleted | tinyint(1) | None |  | 
  | 7 | DeleterUserId | bigint | None |  | 
  | 8 | DeletionTime | datetime(6) | None |  | 
  | 9 | AuthenticationSource | varchar(64) | None |  | 
  | 10 | UserName | varchar(256) | None |  | 
  | 11 | TenantId | int | None |  | 
  | 12 | EmailAddress | varchar(256) | None |  | 
  | 13 | Name | varchar(64) | None |  | 
  | 14 | Surname | varchar(64) | None |  | 
  | 15 | Password | varchar(128) | None |  | 
  | 16 | EmailConfirmationCode | varchar(328) | None |  | 
  | 17 | PasswordResetCode | varchar(328) | None |  | 
  | 18 | LockoutEndDateUtc | datetime(6) | None |  | 
  | 19 | AccessFailedCount | int | None |  | 
  | 20 | IsLockoutEnabled | tinyint(1) | None |  | 
  | 21 | PhoneNumber | varchar(32) | None |  | 
  | 22 | IsPhoneNumberConfirmed | tinyint(1) | None |  | 
  | 23 | SecurityStamp | varchar(128) | None |  | 
  | 24 | IsTwoFactorEnabled | tinyint(1) | None |  | 
  | 25 | IsEmailConfirmed | tinyint(1) | None |  | 
  | 26 | IsActive | tinyint(1) | None |  | 
  | 27 | NormalizedUserName | varchar(256) | None |  | 
  | 28 | NormalizedEmailAddress | varchar(256) | None |  | 
  | 29 | ConcurrencyStamp | varchar(128) | None |  | 
  | 30 | ProfilePictureId | char(36) | None |  | 
  | 31 | ShouldChangePasswordOnNextLogin | tinyint(1) | None |  | 
  | 32 | SignInTokenExpireTimeUtc | datetime(6) | None |  | 
  | 33 | SignInToken | longtext | None |  | 
  | 34 | GoogleAuthenticatorKey | longtext | None |  | 
 #### abpusertokens 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | TenantId | int | None |  | 
  | 3 | UserId | bigint | None |  | 
  | 4 | LoginProvider | varchar(128) | None |  | 
  | 5 | Name | varchar(128) | None |  | 
  | 6 | Value | varchar(512) | None |  | 
  | 7 | ExpireDate | datetime(6) | None |  | 
 #### abpwebhookevents 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | char(36) | None |  | 
  | 2 | WebhookName | longtext | None |  | 
  | 3 | Data | longtext | None |  | 
  | 4 | CreationTime | datetime(6) | None |  | 
  | 5 | TenantId | int | None |  | 
  | 6 | IsDeleted | tinyint(1) | None |  | 
  | 7 | DeletionTime | datetime(6) | None |  | 
 #### abpwebhooksendattempts 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | char(36) | None |  | 
  | 2 | WebhookEventId | char(36) | None |  | 
  | 3 | WebhookSubscriptionId | char(36) | None |  | 
  | 4 | Response | longtext | None |  | 
  | 5 | ResponseStatusCode | int | None |  | 
  | 6 | CreationTime | datetime(6) | None |  | 
  | 7 | LastModificationTime | datetime(6) | None |  | 
  | 8 | TenantId | int | None |  | 
 #### abpwebhooksubscriptions 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | char(36) | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | TenantId | int | None |  | 
  | 5 | WebhookUri | longtext | None |  | 
  | 6 | Secret | longtext | None |  | 
  | 7 | IsActive | tinyint(1) | None |  | 
  | 8 | Webhooks | longtext | None |  | 
  | 9 | Headers | longtext | None |  | 
 #### appbinaryobjects 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | char(36) | None |  | 
  | 2 | TenantId | int | None |  | 
  | 3 | Bytes | longblob | None |  | 
 #### appchatmessages 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | UserId | bigint | None |  | 
  | 3 | TenantId | int | None |  | 
  | 4 | TargetUserId | bigint | None |  | 
  | 5 | TargetTenantId | int | None |  | 
  | 6 | Message | longtext | None |  | 
  | 7 | CreationTime | datetime(6) | None |  | 
  | 8 | Side | int | None |  | 
  | 9 | ReadState | int | None |  | 
  | 10 | ReceiverReadState | int | None |  | 
  | 11 | SharedMessageId | char(36) | None |  | 
 #### appfriendships 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | UserId | bigint | None |  | 
  | 3 | TenantId | int | None |  | 
  | 4 | FriendUserId | bigint | None |  | 
  | 5 | FriendTenantId | int | None |  | 
  | 6 | FriendUserName | varchar(256) | None |  | 
  | 7 | FriendTenancyName | longtext | None |  | 
  | 8 | FriendProfilePictureId | char(36) | None |  | 
  | 9 | State | int | None |  | 
  | 10 | CreationTime | datetime(6) | None |  | 
 #### appinvoices 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | InvoiceNo | longtext | None |  | 
  | 3 | InvoiceDate | datetime(6) | None |  | 
  | 4 | TenantLegalName | longtext | None |  | 
  | 5 | TenantAddress | longtext | None |  | 
  | 6 | TenantTaxNo | longtext | None |  | 
 #### appsubscriptionpayments 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | IsDeleted | tinyint(1) | None |  | 
  | 7 | DeleterUserId | bigint | None |  | 
  | 8 | DeletionTime | datetime(6) | None |  | 
  | 9 | Description | longtext | None |  | 
  | 10 | Gateway | int | None |  | 
  | 11 | Amount | decimal(65,30) | None |  | 
  | 12 | Status | int | None |  | 
  | 13 | EditionId | int | None |  | 
  | 14 | TenantId | int | None |  | 
  | 15 | DayCount | int | None |  | 
  | 16 | PaymentPeriodType | int | None |  | 
  | 17 | ExternalPaymentId | varchar(255) | None |  | 
  | 18 | InvoiceNo | longtext | None |  | 
  | 19 | IsRecurring | tinyint(1) | None |  | 
  | 20 | SuccessUrl | longtext | None |  | 
  | 21 | ErrorUrl | longtext | None |  | 
  | 22 | EditionPaymentType | int | None |  | 
 #### appsubscriptionpaymentsextensiondata 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | SubscriptionPaymentId | bigint | None |  | 
  | 3 | Key | varchar(255) | None |  | 
  | 4 | Value | longtext | None |  | 
  | 5 | IsDeleted | tinyint(1) | None |  | 
 #### appuserdelegations 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | bigint | None |  | 
  | 2 | CreationTime | datetime(6) | None |  | 
  | 3 | CreatorUserId | bigint | None |  | 
  | 4 | LastModificationTime | datetime(6) | None |  | 
  | 5 | LastModifierUserId | bigint | None |  | 
  | 6 | IsDeleted | tinyint(1) | None |  | 
  | 7 | DeleterUserId | bigint | None |  | 
  | 8 | DeletionTime | datetime(6) | None |  | 
  | 9 | SourceUserId | bigint | None |  | 
  | 10 | TargetUserId | bigint | None |  | 
  | 11 | TenantId | int | None |  | 
  | 12 | StartTime | datetime(6) | None |  | 
  | 13 | EndTime | datetime(6) | None |  | 
 #### areas 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(64) | None |  | 
  | 3 | Spell | varchar(64) | None |  | 
  | 4 | Deleted | tinyint(1) | None |  | 
  | 5 | CityId | int | None |  | 
  | 6 | Published | tinyint(1) | 0 |  | 
 #### cities 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(64) | None |  | 
  | 3 | Spell | varchar(64) | None |  | 
  | 4 | Deleted | tinyint(1) | None |  | 
  | 5 | ProvinceId | int | None |  | 
  | 6 | Published | tinyint(1) | 0 |  | 
 #### deploysites 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(128) | None |  | 
  | 3 | Location | varchar(256) | None |  | 
  | 4 | Ip | varchar(64) | None |  | 
  | 5 | Port | int | None |  | 
  | 6 | CreationTime | datetime(6) | None |  | 
  | 7 | ProvinceId | int | None |  | 
  | 8 | CityId | int | None |  | 
  | 9 | AreaId | int | None |  | 
 #### devicegroups 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | TenantId | int | None |  | 
  | 3 | Name | varchar(128) | None |  | 
  | 4 | CreationTime | datetime(6) | None |  | 
  | 5 | Published | tinyint(1) | None |  | 
  | 6 | Deleted | tinyint(1) | 0 |  | 
 #### devices 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | TenantId | int | None |  | 
  | 3 | Name | varchar(128) | None |  | 
  | 4 | Ip | varchar(64) | None |  | 
  | 5 | Serial | varchar(128) | None |  | 
  | 6 | MacAddress | varchar(128) | None |  | 
  | 7 | IsPrint | tinyint(1) | None |  | 
  | 8 | IsCopy | tinyint(1) | None |  | 
  | 9 | IsScan | tinyint(1) | None |  | 
  | 10 | IsColor | tinyint(1) | None |  | 
  | 11 | IsDuplex | tinyint(1) | None |  | 
  | 12 | DeviceStatusId | int | None |  | 
  | 13 | CreationTime | datetime(6) | None |  | 
  | 14 | DeploySiteId | int | None |  | 
  | 15 | Deleted | tinyint(1) | 0 |  | 
  | 16 | DeviceGroupId | int | 0 |  | 
  | 17 | InitialValue | int | 0 |  | 
  | 18 | ManufactureId | int | 0 |  | 
  | 19 | ManufacturerFkId | int | None |  | 
  | 20 | Published | tinyint(1) | 0 |  | 
  | 21 | VersionId | int | 0 |  | 
 #### fields 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(128) | None |  | 
  | 3 | Code | varchar(128) | None |  | 
  | 4 | JsUrl | varchar(256) | None |  | 
  | 5 | IsScript | tinyint(1) | None |  | 
  | 6 | AlarmTypeId | int | None |  | 
  | 7 | CreationTime | datetime(6) | None |  | 
 #### fieldvalues 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Key | varchar(128) | None |  | 
  | 3 | Value | varchar(128) | None |  | 
  | 4 | Description | varchar(256) | None |  | 
  | 5 | CreationTime | datetime(6) | None |  | 
  | 6 | DeviceId | int | None |  | 
  | 7 | FieldId | int | None |  | 
 #### manufacturers 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(128) | None |  | 
  | 3 | Description | varchar(256) | None |  | 
  | 4 | Published | tinyint(1) | None |  | 
  | 5 | Deleted | tinyint(1) | None |  | 
  | 6 | DisplayOrder | int | None |  | 
  | 7 | CreationTime | datetime(6) | None |  | 
 #### objectidentifies 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(128) | None |  | 
  | 3 | Length | int | None |  | 
  | 4 | Description | varchar(256) | None |  | 
  | 5 | AlarmTypeId | int | None |  | 
  | 6 | CreationTime | datetime(6) | None |  | 
  | 7 | VersionGroupId | int | 0 |  | 
 #### objectidentifygroups 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(64) | None |  | 
  | 3 | Description | varchar(256) | None |  | 
  | 4 | CreationTime | datetime(6) | None |  | 
 #### objectidentifyobjectidentifygroupmappings 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | ObjectIdentifyId | int | None |  | 
  | 3 | ObjectIdentifyGroupId | int | None |  | 
 #### provinces 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(64) | None |  | 
  | 3 | Spell | varchar(64) | None |  | 
  | 4 | Deleted | tinyint(1) | None |  | 
  | 5 | Published | tinyint(1) | 0 |  | 
 #### templates 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(64) | None |  | 
  | 3 | Description | varchar(256) | None |  | 
  | 4 | CreationTime | datetime(6) | None |  | 
 #### versiongroups 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(128) | None |  | 
  | 3 | Description | varchar(256) | None |  | 
  | 4 | CreationTime | datetime(6) | None |  | 
  | 5 | ManufacturerId | int | None |  | 
 #### versions 
 | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |
 | --- | --- | --- | --- | --- |
  | 1 | Id | int | None |  | 
  | 2 | Name | varchar(128) | None |  | 
  | 3 | Description | varchar(256) | None |  | 
  | 4 | CreationTime | datetime(6) | None |  | 
  | 5 | VersionGroupId | int | None |  | 
 